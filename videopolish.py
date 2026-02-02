import os
import subprocess
import tempfile
from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx
from tqdm import tqdm

INPUT_DIR = "input_videos"
OUTPUT_DIR = "output_videos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ======================
# SETTINGS
# ======================
TARGET_HEIGHT = 1920      # TikTok / Reels (use 1080 for YouTube)
VIDEO_BITRATE = "16M"
AUDIO_BOOST_DB = 5

# ======================
# PROCESS EACH VIDEO
# ======================
for file in tqdm(os.listdir(INPUT_DIR)):
    if not file.lower().endswith((".mp4", ".mov", ".mkv")):
        continue

    input_path = os.path.join(INPUT_DIR, file)
    base = os.path.splitext(file)[0]
    output_path = os.path.join(OUTPUT_DIR, f"{base}_FINAL.mp4")
    caption_path = os.path.join(OUTPUT_DIR, f"{base}.srt")

    clip = VideoFileClip(input_path)

    # ======================
    # 🎞️ FILM LOOK
    # ======================
    video = (
        clip
        .resize(height=TARGET_HEIGHT)
        .fx(vfx.colorx, 1.12)
        .fx(vfx.lum_contrast, contrast=0.3)
        .fx(vfx.sharpen, 1.2)
    )

    # ======================
    # TEMP FILES
    # ======================
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        raw_audio = f.name

    video.audio.write_audiofile(raw_audio, fps=44100)

    enhanced_audio = raw_audio.replace(".wav", "_enhanced.wav")

    # ======================
    # 🎧 AI SPEECH ENHANCEMENT
    # ======================
    subprocess.run([
        "resemble-enhance",
        raw_audio,
        enhanced_audio
    ], check=False)

    # ======================
    # 🎤 SILENCE REMOVAL + 🎙️ COMPRESSION + EQ
    # ======================
    final_audio = enhanced_audio.replace(".wav", "_final.wav")

    subprocess.run([
        "ffmpeg", "-y",
        "-i", enhanced_audio,
        "-af",
        (
            "silenceremove=start_periods=1:start_silence=0.4:start_threshold=-40dB,"
            "acompressor=threshold=-18dB:ratio=3:attack=5:release=80,"
            "equalizer=f=3000:t=q:w=1.2:g=4,"
            f"volume={AUDIO_BOOST_DB}dB"
        ),
        final_audio
    ], check=True)

    # ======================
    # 📱 AUTO CAPTIONS (WHISPER)
    # ======================
    subprocess.run([
        "whisper",
        raw_audio,
        "--model", "medium",
        "--language", "en",
        "--output_format", "srt",
        "--output_dir", OUTPUT_DIR
    ], check=True)

    # ======================
    # 🎬 FINAL EXPORT (GPU)
    # ======================
    video.set_audio(VideoFileClip(final_audio).audio).write_videofile(
        output_path,
        codec="h264_nvenc",
        audio_codec="aac",
        preset="p4",
        fps=clip.fps,
        ffmpeg_params=[
            "-b:v", VIDEO_BITRATE,
            "-maxrate", "18M",
            "-bufsize", "24M",
            "-profile:v", "high"
        ]
    )

    # Cleanup
    for f in [raw_audio, enhanced_audio, final_audio]:
        if os.path.exists(f):
            os.remove(f)

print("🔥 ALL VIDEOS PROCESSED SUCCESSFULLY")
