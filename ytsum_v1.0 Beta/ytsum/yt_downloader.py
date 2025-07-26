import yt_dlp
from pathlib import Path

def download_audio(url: str) -> str:
    output_path = Path("downloads")
    output_path.mkdir(exist_ok=True)

    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_file = output_path / f"{info['id']}.mp3"

    if audio_file.exists():
        print(f"File already exists: {audio_file}, skipping download.")
        return str(audio_file)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(output_path / '%(id)s.%(ext)s'),
        'quiet': True,
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return str(audio_file)
