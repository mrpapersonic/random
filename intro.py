import os

amt = 1
for subdir, dirs, files in os.walk("./"):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        if ext == ".mkv":
            os.system(f'ffmpeg -i "{file}" -t 30 -pix_fmt yuv420p "Clips\intro_{amt}.mp4')
            amt += 1
