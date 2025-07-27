from yt_downloader import download_audio
from transcriber import transcribe_audio
from summarizer import summarize_text
from rich.console import Console

console = Console()

def main(url: str):
    console.print("[bold blue]Downloading audio...[/]")
    audio_path = download_audio(url)

    console.print("[bold blue]Transcribing with Whisper Tiny...[/]")
    transcript = transcribe_audio(audio_path)

    console.print("[bold blue]Summarizing with Gemini...[/]")
    summary = summarize_text(transcript, audio_path)

    console.print("[bold green]Summary:[/]\n" + summary)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_url>")
    else:
        main(sys.argv[1])
