#!/usr/bin/python
# Binaries from
# https://github.com/ungoogled-software/ungoogled-chromium-archlinux/
import urllib.request
import os
import json
import sys
import subprocess
from tqdm import tqdm


# Decodes subprocess stdouts, made into a function because why not
def decode_line(line):
    decodeline = []
    for i in line:
        decodeline.append(i.decode("utf-8").rstrip())
    return decodeline


# Checks current version against installed version
def check_version(version):
    pacman = subprocess.Popen(["pacman", "-Qm"], stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
    decodeline = decode_line(pacman.stdout.readlines())
    for i in decodeline:
        if i.split(" ")[0] == "ungoogled-chromium":
            if i.split(" ")[1] == version:
                print("You are on the latest version!")
                sys.exit(0)


# Checks for any Chromium processes currently running
# Returns 0 if running, 1 if not running, and 2 if it doesn't exist
def check_for_file(files):
    process = subprocess.Popen(["which", files], stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)
    process.wait()

    if process.returncode == 0:
        pgrep = subprocess.Popen(["pidof", files], stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        decodeline = decode_line(pgrep.stdout.readlines())
        if len(decodeline) > 0:
            return 0
        else:
            return 1
    else:
        return 2


# Progress bar, copied from stackoverflow :pngtroll:
class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path,
                                   reporthook=t.update_to)


if check_for_file("chromium") == 0:
    print("Chromium is still running! Exiting...")
    sys.exit(1)
owner = "ungoogled-software"
repo = "ungoogled-chromium-archlinux"
json = json.loads(urllib.request.urlopen(f"https://api.github.com/repos/{owner}/{repo}/releases").read())
check_version(json[0]["tag_name"])
for i in json[0]["assets"]:
    if i["content_type"] == "application/octet-stream":
        download_url(f"{i['browser_download_url']}", "/tmp/chromium.tar.zst")
os.system("sudo pacman -U /tmp/chromium.tar.zst")
os.remove("/tmp/chromium.tar.zst")
