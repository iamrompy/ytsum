import requests
import os
from dotenv import load_dotenv
from rich.progress import Progress, SpinnerColumn, TextColumn
from pathlib import Path

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def summarize_text(text: str, audio_path: str) -> str:
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": f"Summarize this transcript:\n\n{text}"}]
        }]
    }

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
        task = progress.add_task(description="Summarizing with Gemini...", total=None)
        response = requests.post(f"{GEMINI_URL}?key={API_KEY}", headers=headers, json=payload)

    response.raise_for_status()
    summary = response.json()['candidates'][0]['content']['parts'][0]['text']

    summary_dir = Path("summaries")
    summary_dir.mkdir(exist_ok=True)
    base = Path(audio_path).stem
    summary_path = summary_dir / f"sum_{base}.txt"
    summary_path.write_text(summary, encoding="utf-8")

    return summary
