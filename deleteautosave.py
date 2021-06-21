import os

for file in os.listdir("./"):
    name = os.path.splitext(file)[0][:-16][-8:]
    if name == "AutoSave":
        os.remove(file)
