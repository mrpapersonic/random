import os, sys, zlib

def crc(filename): return "%X"%(zlib.crc32(open(filename,"rb").read()) & 0xFFFFFFFF)

try:
    temp = sys.argv[1]
except:
    print("No file specified!")
    sys.exit()

f = open(sys.argv[1])
lines = f.readlines()
f.close()

for line in lines:
    if not line[0] == ";":
        crc32 = line.strip()[-8:]
        name = line.strip()[:-8]
        if crc(name).zfill(8) == crc32:
            print(f"{name}: CRC hash match!")
        else:
            print(f"{name}: CRC hash does not match!")
