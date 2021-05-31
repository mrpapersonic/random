import os, sys

count = 0
for path, folder, files in os.walk("./"):
    for file in files:
        if file.endswith('.mkv'):
            count += 1
            file_mod = file[:len(file) - 15]
            file_mod = f'KIZNAIVER - {count:02} [{file_mod[7:]}]'
            os.system(f'mkvmerge -o "output\{file_mod}.mkv" --audio-tracks 2 --subtitle-tracks 6 "{file}"')
            os.system(f'mkvpropedit --delete-attachment mime-type:image/jpeg "output\{file_mod}.mkv"')