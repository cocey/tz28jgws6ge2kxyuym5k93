from pyquery import PyQuery as pq
import requests
import os

urls = [
    "https://mp3semti.com/album/Kan-Kokusu-1998"
]

for url in urls:
    print(url)

    r = requests.get(url)
    d = pq(r.content)

    artist = str(d(".Mp3DetayBlok")).split("/sarkici/")[1].split('"')[0]
    album = url.split("/")[-1]
    links = []

    for a in str(d(".ortaMp3lerListesi li a")).split('href="')[1:]:
        path = a.split('"')[0]
        links.append(url.split("/album/")[0]+path)
    if not os.path.exists(os.path.join("data/new", artist)):
        os.makedirs(os.path.join("data/new", artist))
    with open(os.path.join("data/new", artist, album), "w+") as f:
        f.write("\n".join(links))
