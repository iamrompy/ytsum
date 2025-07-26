# 🎧 ytsum – YouTube Transcriber + Summarizer

**ytsum** is a lightweight command-line tool that:
- Downloads audio from a YouTube video
- Transcribes it using Whisper Tiny (faster-whisper)
- Summarizes the transcript using Gemini 2.0 Flash (via Google AI Studio API)
- Shows real-time progress bars
- Skips already-processed files
- Saves transcripts and summaries for reuse

---

## 📦 Requirements

- Python 3.10+
- FFmpeg (for `yt-dlp`)
- Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 🚀 Setup

### 1. Clone or download the repo

```bash
git clone https://github.com/yourusername/ytsum.git
cd ytsum
```

Or unzip the provided folder if you received a `ytsum.zip`.

---

### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

---

### 3. Set up `.env` with your Gemini API key

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

### 4. Run the tool

```bash
python main.py "https://www.youtube.com/watch?v=your_video_id"
```

---

## 📁 Outputs

- 🎙️ **Audio**: saved in `downloads/`
- 📝 **Transcript**: saved in `transcripts/<video_id>.txt`
- ✨ **Summary**: saved in `summaries/sum_<video_id>.txt`

Already downloaded or transcribed files are **skipped automatically**.

---

## ✅ Features

- ✅ Whisper Tiny (via faster-whisper) for local, fast transcription
- ✅ Gemini 2.0 Flash API for smart summaries
- ✅ Progress bars for both steps using `rich`
- ✅ Auto-skip existing `.mp3` and `.txt` files
- ✅ Clear directory structure

---

## 🛠️ Troubleshooting

- If you see `libtorchaudio.pyd not found`, make sure you're **not importing torchaudio**
- If you get `404` errors from Gemini, double-check:
  - You're using the **v1beta** endpoint
  - Model: `gemini-2.0-flash`
  - Key is from [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 📚 Roadmap Ideas

- [ ] Long video chunking
- [ ] Chapter-style summaries
- [ ] GUI version (Gradio/Tkinter)
- [ ] Batch mode for playlists

---

## 🤝 License

MIT — use freely, credit if useful.
