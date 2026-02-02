from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx

/*
What this code will do:
🎨 Visual polish: brighter colors, better contrast, sharper look 
🔊 Audio cleanup: reduce noise, boost voice, balance sound
*/

input_path = "/mnt/data/video.mp4"
output_path = "/mnt/data/Video_polished.mp4"

# Load video
clip = VideoFileClip(input_path)

# Visual polish: increase brightness, contrast, sharpness
video_polished = (
    clip
    .fx(vfx.colorx, 1.15)      # brighter colors
    .fx(vfx.lum_contrast, lum=0, contrast=0.2)  # better contrast
    .fx(vfx.sharpen)           # sharper look
)

# Audio cleanup: normalize and boost voice
audio_polished = (
    video_polished.audio
    .fx(afx.audio_normalize)
    .fx(afx.volumex, 1.2)
)

final_clip = video_polished.set_audio(audio_polished)

# Export
final_clip.write_videofile(
    output_path,
    codec="libx264",
    audio_codec="aac",
    temp_audiofile="/mnt/data/temp-audio.m4a",
    remove_temp=True
)

output_path
