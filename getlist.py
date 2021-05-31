import urllib.request, json, re, sys

id = input("What is the MyAnimeList ID for your anime?: ")
try:
    temp = int(id)
except:
    print("Not a valid MyAnimeList ID! Exiting.")
    sys.exit()

with urllib.request.urlopen(f"https://api.jikan.moe/v3/anime/{str(id)}/episodes") as url:
    data = json.loads(url.read().decode())
    count = 0
    for i in range(len(data["episodes"])):
        if count == 0:
            f = open("list.txt", "w", encoding="utf-8")
        else:
            f = open("list.txt", "a", encoding="utf-8")
        """
        this is really hard to read at first glance so i'll break it down
        it replaces "?" and ":" with legal counterparts so windows stops screaming
        then strips among a dash (which usually shows different parts in an episode)
        it then removes the last part of the string cause most, if not of MAL's have spaces before slashes
        """
        f.write(data["episodes"][count]["title"].replace("?", "？").replace(":", "꞉").replace('"', "“").split("/")[0].rstrip() + "\n")
        count += 1
        f.close()
