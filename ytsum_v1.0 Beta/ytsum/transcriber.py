from faster_whisper import WhisperModel
from rich.progress import Progress, TimeElapsedColumn, BarColumn, TextColumn
from pathlib import Path

model = WhisperModel("tiny", compute_type="int8")

def transcribe_audio(audio_path: str) -> str:
    transcript_dir = Path("transcripts")
    transcript_dir.mkdir(exist_ok=True)

    base = Path(audio_path).stem
    txt_path = transcript_dir / f"{base}.txt"

    if txt_path.exists():
        print(f"Transcript already exists: {txt_path}, skipping transcription.")
        return txt_path.read_text(encoding="utf-8")

    segments_gen, _ = model.transcribe(audio_path, word_timestamps=False)

    transcript = []
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        transient=True
    ) as progress:
        task = progress.add_task("[cyan]Transcribing...", total=None)
        for seg in segments_gen:
            transcript.append(seg.text)
            progress.advance(task)

    transcript_text = " ".join(transcript)
    txt_path.write_text(transcript_text, encoding="utf-8")
    return transcript_text
