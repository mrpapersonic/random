import os
import sys

# valid filename: "[title] - [episode number].mkv"
for file in os.listdir("./"):
    if file.endswith(".mkv"):
        name = file[:-9]

try:
    throwaway = open(f"{name} - 01.mkv", 'rb')
except OSError:
    print(f'Could not open "{name} - 01.mkv". Are you sure the file exists?')
    sys.exit()
throwaway.close()

titles = open('list.txt', 'r', encoding='utf-8')
titlelist = titles.readlines()
titles.close()

count = 1
for line in titlelist:
    line = line.rstrip("\n")
    if int(count) <= 9:
        os.rename(f'{name} - 0{count}.mkv', f'{name} - 0{count} [{line}].mkv')
    else:
        os.rename(f'{name} - {count}.mkv', f'{name} - {count} [{line}].mkv')
    count += 1
