import os
import ffmpeg

amt = 1
for files in os.walk("./"):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        if ext == ".mkv":
            stream = ffmpeg.input(file)
            os.system(
                f'ffmpeg -i "{file}" -t 30 -pix_fmt yuv420p "Clips\intro_{amt}.mp4')
            amt += 1
