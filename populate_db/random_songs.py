# Code mostly taken from and changed from js to py: (token also was taken)
# https://codepen.io/bobhami/pen/gwrJNp
import sqlite3
import random
import requests

CLIENTID = "Eq8KSecb2Yz4Lq--EUjuGWH_8OifHCRwdwHr1ztKdLx5Qk_zCZG--AXPSQzMXhL-"
CLIENTSECRET = "-3Ynmxt9BZab3Qs5sbr_GdzGxXoGqSqbSISFuEQwquYeVm-5-A3nFIcgUOvDSY731GT-hhJtvTK5jYDccT7juQ"
accessToken = "?access_token=CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx"
API = "https://api.genius.com/search"
APISong = "https://api.genius.com/songs/"
songID = "2471960"
maxSong = 2471960
con = sqlite3.connect("../data.db")


def getRandomSong() -> dict:

    songID = str(random.randint(1, maxSong))

    headers = {
        "User-agent": "lol",
        "Accept": "application/json"
    }
    request = requests.get(APISong+songID+accessToken, headers=headers)

    if (request.status_code == 404):
        print("404")
        return getRandomSong()

    json = request.json()

    song = json['response']['song']
    return song


for i in range(10):
    print(f"Added song {i+1}")
    song = getRandomSong()
    title = song.get('title')
    artist = song.get('artist_names')
    image_url = song.get('song_art_image_url')

    image_id = None
    if image_url:
        con.execute("INSERT INTO Images (image_url, alt) VALUES (?, ?)",
                    (image_url, "Album art for "+title))
        image_id = con.execute("SELECT last_insert_rowid()").fetchone()[0]

    con.execute("INSERT INTO MusicMetadata (title, artist, image_id) VALUES (?, ?, ?)",
                (title, artist, image_id))

con.commit()
