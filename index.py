import requests
import os


def downloadFile(url, outputFolder):
    localFilename = url.split('/')[-1]
    print("downloading:", url)
    target = os.path.join(outputFolder, localFilename)
    if not os.path.exists(target):
        r = requests.get(url, allow_redirects=True)
        open(os.path.join(outputFolder, localFilename), 'wb').write(r.content)


outputFolder = "./output/"

dataFolder = "data/queue"


def downloadAlbum(artist, album):
    targetFolder = os.path.join(outputFolder, artist, album)
    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)

    prefix = "https://mp3semticdn.com/mp3_files/"+artist+"/"+album+"/"
    with open(os.path.join(dataFolder, artist, album), "r") as f:
        for url in f.readlines():
            downloadFile(
                prefix+url.split("/")[-1].replace("\n", "").replace(".html", ".mp3"), targetFolder)


for artist in os.listdir(dataFolder):
    if os.path.isdir(os.path.join(dataFolder, artist)):
        print("artist:", artist)
        for album in os.listdir(os.path.join(dataFolder, artist)):
            if album != ".DS_Store":
                print("album:", album)
                downloadAlbum(artist, album)
