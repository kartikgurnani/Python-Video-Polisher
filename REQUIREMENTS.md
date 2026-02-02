
```
**REQUIREMENTS.md**
```

---

````markdown
# 📋 Requirements👍

This document lists all system, hardware, and software requirements needed to run the **Python Video Polisher** pipeline successfully.

---

## 🖥️ System Requirements

### Operating System
- macOS 12+
- Ubuntu 20.04+
- Windows 10/11 (WSL2 recommended)

> Linux or macOS is strongly recommended for best FFmpeg and GPU support.

---

## 🐍 Python Requirements

- Python **3.9 or higher**
- `pip` (latest version recommended)

Verify your Python version:
```bash
python --version
````

---

## 🎬 FFmpeg (Required)

FFmpeg is **mandatory** and must be accessible from the command line.

### Minimum FFmpeg Requirements

* Audio filters: `silenceremove`, `acompressor`, `equalizer`
* Video encoding: `libx264`

### Recommended (GPU Acceleration)

* NVIDIA GPU with **NVENC** support
* FFmpeg compiled with `h264_nvenc`

Verify NVENC support:

```bash
ffmpeg -encoders | grep nvenc
```

---

## 🎮 Hardware Requirements

### Minimum

* 8 GB RAM
* Multi-core CPU
* SSD storage recommended

### Recommended

* NVIDIA GPU (RTX / GTX series)
* 16 GB+ RAM
* CUDA-compatible drivers

> GPU is optional but **significantly improves render speed** and AI audio performance.

---

## 📦 Python Dependencies

### Core Dependencies

```text
moviepy
numpy
scipy
pydub
noisereduce
tqdm
```

### AI & Captioning

```text
openai-whisper
pysrt
```

### Optional (AI Speech Enhancement)

```text
resemble-enhance
demucs
```

Install required dependencies:

```bash
pip install moviepy numpy scipy pydub noisereduce tqdm openai-whisper pysrt
```

Optional AI enhancement tools:

```bash
pip install resemble-enhance demucs
```

---

## 🤖 AI Models

### Whisper (Captions)

* Default model: `medium`
* Supported models: `small`, `medium`, `large`

Model trade-offs:

| Model  | Speed      | Accuracy |
| ------ | ---------- | -------- |
| small  | ⚡ Fast     | ⭐⭐       |
| medium | ⚖ Balanced | ⭐⭐⭐      |
| large  | 🐢 Slow    | ⭐⭐⭐⭐     |

---

## 🔊 Audio Processing Notes

* Background noise is learned from the first second of audio
* Silence detection threshold: `-40 dB` (configurable)
* Speech clarity boost centered at `~3 kHz`
* Compression optimized for spoken voice (podcast-style)

---

## 📱 Platform Optimization

| Platform       | Resolution           | Codec |
| -------------- | -------------------- | ----- |
| TikTok / Reels | 9:16 (1920px height) | H.264 |
| YouTube        | 16:9 (1080p+)        | H.264 |
| Shorts         | 9:16                 | H.264 |

---

## ⚠️ Known Limitations

* AI speech enhancement may fail without GPU
* Heavy music may affect silence detection accuracy
* Extremely poor recordings cannot be fully restored

---

## 📄 License

This project is licensed under the **MIT License**.

See the full license details here:
[https://github.com/kartikgurnani/Python-Video-Polisher/](https://github.com/kartikgurnani/Python-Video-Polisher/#)

---

## 🆘 Troubleshooting

### FFmpeg not found

```bash
sudo apt install ffmpeg
```

### Whisper slow or crashing

* Use a smaller model (`small`)
* Ensure sufficient RAM
* Enable GPU if available

---

## 📬 Support

If you encounter issues:

* Verify FFmpeg installation
* Check Python version
* Review logs carefully

Pull requests and improvements are welcome.

---
