import os

titles = open('list.txt', 'r')
titlelist = titles.readlines()
titles.close()

count = 1
for line in titlelist:
    line = line.rstrip("\n")
    if int(count) <= 9:
        os.rename(f'Lucky☆Star - 0{count}.mkv', f'Lucky☆Star - 0{count} [{line}].mkv')
    else:
        os.rename(f'Lucky☆Star - {count}.mkv', f'Lucky☆Star - {count} [{line}].mkv')
    count += 1
