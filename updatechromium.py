# https://github.com/ungoogled-software/ungoogled-chromium-archlinux/
import urllib.request
import os
import json
import sys
import subprocess
from tqdm import tqdm

# Returns 0 if running, 1 if not running, and 2 if it doesn't exist
def check_for_file(file):
    process = subprocess.Popen(["which", file], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    process.wait()

    if process.returncode == 0:
        try:
            subprocess.check_output(["pidof", file])
            return 0
        except:
            return 1
    else:
        return 2

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

if check_for_file("chromium") == 0:
    print("Chromium is still running! Exiting...")
    sys.exit(1)
OWNER = "ungoogled-software"
REPO = "ungoogled-chromium-archlinux"
r = urllib.request.urlopen(f"https://api.github.com/repos/{OWNER}/{REPO}/releases")
json = json.loads(r.read())
for i in json[0]["assets"]:
    if i["content_type"] == "application/octet-stream":
        download_url(f"{i['browser_download_url']}", "/tmp/chromium.tar.zst")
os.system("sudo pacman -U /tmp/chromium.tar.zst")
os.remove("/tmp/chromium.tar.zst")

