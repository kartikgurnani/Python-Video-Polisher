# 🎬 Cinematic Video Processing Pipeline

A production-grade, automated video post-processing pipeline built in Python.  
Designed for creators, developers, and media teams who want **cinematic visuals**, **studio-quality audio**, **AI-powered speech cleanup**, and **auto captions** — all in batch, all accelerated by GPU.

---

## ✨ Features

### 🎞️ Cinematic Video
- Film-style color grading
- Enhanced contrast, saturation, and sharpness
- Optimized for YouTube, TikTok, Reels, and Shorts
- Automatic vertical resize for social platforms

### 🔊 Professional Audio
- Real noise reduction (not just normalization)
- Automatic silence removal (dead air trimming)
- Podcast-grade voice compression
- Speech clarity EQ (2–4 kHz boost)
- Optional AI speech enhancement

### 🤖 AI-Powered
- AI speech enhancement (echo & room noise reduction)
- Automatic captions using OpenAI Whisper (`.srt`)
- Language detection & transcription

### 🚀 Performance
- GPU-accelerated video encoding (NVENC)
- Batch processing for multiple videos
- Fully automated end-to-end workflow

---

## 📁 Project Structure

```text
.
├── input_videos/        # Drop raw videos here
├── output_videos/       # Processed videos + captions
├── process_videos.py    # Main pipeline script
└── README.md


⚙️ Requirements
System
> Python 3.9+
> FFmpeg (with NVENC support recommended)
> NVIDIA GPU (optional but strongly recommended)


> Verify NVENC support:

ffmpeg -encoders | grep nvenc


📦 Installation
Python dependencies
## pip install moviepy pydub noisereduce numpy scipy tqdm openai-whisper pysrt
Optional (AI Speech Enhancement)
## pip install resemble-enhance demucs


▶️ Usage

Place videos inside the input_videos/ folder
Run the script:

python videopolish.py

Outputs will appear in output_videos/:
Final rendered videos (*_FINAL.mp4)
Auto-generated captions (.srt)


🎛️ Configuration

Inside the script:

TARGET_HEIGHT = 1920   # 1920 for TikTok/Reels, 1080 for YouTube
VIDEO_BITRATE = "16M"
AUDIO_BOOST_DB = 5

Platform presets

TikTok / Reels: TARGET_HEIGHT = 1920
YouTube: TARGET_HEIGHT = 1080


🧠 What This Pipeline Is (and Isn’t)

✅ Is
Real audio processing (FFmpeg filters + AI)
Creator-ready automation
Suitable for podcasts, tutorials, talking-head videos
Fast and scalable

❌ Is Not
A replacement for full DAWs or NLEs
Magic audio repair for extremely poor recordings


📱 Auto Captions

Captions are generated using Whisper and saved as .srt.

Change model size for speed vs accuracy:
--model small   # faster
--model medium  # balanced
--model large   # best accuracy


🚧 Known Limitations
- AI speech enhancement tools may require GPU for best results
- Silence removal thresholds may need tuning for music-heavy videos
- Caption language defaults to English (configurable)


🔮 Roadmap (Ideas)
Burn-in captions (TikTok-style)
Jump-cut smoothing
LUT file support
Automatic chapters (YouTube)
Background music ducking

📄 License

MIT License.
Use it, fork it, ship it, make cool stuff.


🙌 Built with:
MoviePy
FFmpeg
Whisper
Pydub
Open-source AI audio tools



---

If you want, I can:
- Tailor this for **open-source vs portfolio**
- Add **badges** (Python, FFmpeg, GPU, MIT)
- Write a **short README** or **enterprise version**
- Create a **docs/USAGE.md**

Just tell me how public this repo is 👌
