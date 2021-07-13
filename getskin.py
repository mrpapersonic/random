# minecraft skin fetcher
# by Paper, 2021-07-13
# this only really exists as reference to a possible java implementation
# (for those beta versions of minecraft that don't support UUIDs)
# however, i do not have any java experience, like, at all
# so that'll be fun!

import argparse
import base64
import cv2
import json
import numpy
import urllib.request

def get_status_code(mcign):
    return urllib.request.urlopen(f"https://api.mojang.com/users/profiles/minecraft/{mcign}").getcode()

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--crop', help='crops your skin to 64x32, for beta versions', action="store_true")
parser.add_argument('-u', '--username', help='minecraft in-game name')
args = parser.parse_args()

# parse username, probably unnecessarily long but idc
if args.username:
    myname = args.username
try:
    statuscode = get_status_code(myname)
except:
    myname = input("What is your Minecraft username?: ")
    statuscode = get_status_code(myname)
finally:
    while statuscode == 204:
        myname = input("What is your Minecraft username?: ")
        statuscode = get_status_code(myname)

skinlink = json.loads(base64.b64decode(json.loads(urllib.request.urlopen(f'https://sessionserver.mojang.com/session/minecraft/profile/{json.loads(urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/{0}".format(myname)).read().decode("utf-8"))["id"]}').read().decode("utf-8"))["properties"][0]["value"]).decode("utf-8"))["textures"]["SKIN"]["url"] # get your free long lines here!
skin = numpy.asarray(bytearray(urllib.request.urlopen(skinlink).read()), dtype="uint8")
skin = cv2.imdecode(skin, cv2.IMREAD_UNCHANGED)

# this is worthless if your skin is already 64x32
if args.crop:
    skin = skin[0:32, 0:64]

# write the final skin
cv2.imwrite("skin.png", skin)
