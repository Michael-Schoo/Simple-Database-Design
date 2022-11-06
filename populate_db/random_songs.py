# Code mostly taken from and changed from js to py: (token also was taken)
# https://codepen.io/bobhami/pen/gwrJNp
import sqlite3
import random
import requests

# Set constants
CLIENTID = "Eq8KSecb2Yz4Lq--EUjuGWH_8OifHCRwdwHr1ztKdLx5Qk_zCZG--AXPSQzMXhL-"
CLIENTSECRET = "-3Ynmxt9BZab3Qs5sbr_GdzGxXoGqSqbSISFuEQwquYeVm-5-A3nFIcgUOvDSY731GT-hhJtvTK5jYDccT7juQ"
accessToken = "?access_token=CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx"
API = "https://api.genius.com/search"
APISong = "https://api.genius.com/songs/"
songID = "2471960"
maxSong = 2471960

# Open database
con = sqlite3.connect("../data.db")


def getRandomSong() -> dict:
    # Get a random song

    # Get a random song id
    songID = str(random.randint(1, maxSong))

    # Set the headers (user agent needed so that the api will accept the request)
    headers = {
        "User-agent": "lol",
        "Accept": "application/json"
    }

    # Get the song
    request = requests.get(APISong+songID+accessToken, headers=headers)

    # If the song is not found, try again
    if (request.status_code == 404):
        print("404")
        return getRandomSong()

    json = request.json()

    # Return the song
    song = json['response']['song']
    return song


for i in range(10):
    # Go through each song and add it to the database
    print(f"Added song {i+1}")
    song = getRandomSong()
    title = song.get('title')
    artist = song.get('artist_names')
    image_url = song.get('song_art_image_url')

    # If there is an image, add it to the database
    image_id = None
    if image_url:
        con.execute("INSERT INTO Images (image_url, alt) VALUES (?, ?)",
                    (image_url, "Album art for "+title))
        image_id = con.execute("SELECT last_insert_rowid()").fetchone()[0]

    # Add the song to the database
    con.execute("INSERT INTO MusicMetadata (title, artist, image_id) VALUES (?, ?, ?)",
                (title, artist, image_id))

con.commit()
