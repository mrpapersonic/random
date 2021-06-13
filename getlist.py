import urllib.request, json, re, sys

# Initialize variables
key = "f090bb54758cabf231fb605d3e3e0468" # https://github.com/xbmc/metadata.themoviedb.org.python/blob/master/python/lib/tmdbscraper/tmdbapi.py#L36

# Ask for source
if not 2 >= len(sys.argv): source = sys.argv[1]
if not 'source' in locals() or not 'source' in globals():
    source = input("Which website would you like to pull titles from? [tmdb, mal]: ")
while source not in ["tmdb", "mal"]:
    print("Not a valid source! Exiting.")
    sys.exit()

# Ask for ID
if not 3 >= len(sys.argv): source = sys.argv[2]
if not 'id' in locals() or not 'id' in globals():
    id = input("What is the ID for your show?: ")
try:
    temp = int(id)
except:
    print("Not a valid ID! Exiting.")
    sys.exit()

# Scrapers
if source == 'tmdb':
    season = input("Which season do you want?: ") # required because api is... odd
    try:
        temp = int(season)
    except:
        print("Not a valid season! Exiting.")
        sys.exit()
    data = json.loads(urllib.request.urlopen(f'https://api.themoviedb.org/3/tv/{str(id)}?api_key={key}').read().decode())
    amount = data["number_of_episodes"]
    f = open("list.txt", "w", encoding="utf-8")
    f.write("")
    f.close()
    count = 1
    for i in range(amount): # this may count as spamming the api but i don't care lol
        with urllib.request.urlopen(f'https://api.themoviedb.org/3/tv/{str(id)}/season/{season}/episode/{count}?api_key={key}') as url:
            data = json.loads(url.read().decode())
            f = open("list.txt", "a", encoding="utf-8")
            f.write(data["name"].replace("?", "？").replace(":", "꞉").replace('"', "“").split("/")[0].rstrip() + "\n")
            count += 1
            f.close()
if source == 'mal':
    with urllib.request.urlopen(f"https://api.jikan.moe/v3/anime/{str(id)}/episodes") as url:
        data = json.loads(url.read().decode())
        count = 0
        f = open("list.txt", "w", encoding="utf-8")
        f.write("")
        f.close()
        for i in range(len(data["episodes"])):
            f = open("list.txt", "a", encoding="utf-8")
            f.write(data["episodes"][count]["title"].replace("?", "？").replace(":", "꞉").replace('"', "“").split("/")[0].rstrip() + "\n")
            count += 1
            f.close()
