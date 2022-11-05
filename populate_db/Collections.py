import sqlite3
con = sqlite3.connect("../data.db")

data = [
    {'user_id': 1, 'name': 'My favorite books', 'description': 'Books that you should read, because I say so', 'created': '2008-11-11 13:23:44'},
    {'user_id': 4, 'name': 'Never read/listen to these', 'description': 'The following art is horrible'},
]


for row in data:
    if ('created' in row):
        con.execute("INSERT INTO Collections (user_id, name, description, created_at) VALUES (?, ?, ?, ?)",
                    (row.get('user_id'), row.get('name'), row.get('description'), row.get('created')))
    else:
        con.execute("INSERT INTO Collections (user_id, name, description) VALUES (?, ?, ?)",
                    (row.get('user_id'), row.get('name'), row.get('description')))

def favoriteBooks():
    # get 10 random books from the BookMetadata table
    books = con.execute("SELECT book_id FROM BookMetadata ORDER BY RANDOM() LIMIT 10").fetchall()

    # add them to the collection+metadata
    for book in books:
        con.execute("INSERT INTO Collections_Metadata (collection_id, book_id) VALUES (?, ?)",
                    (1, book[0]))

def neverRead():
    # get 5 random books from the BookMetadata table
    books = con.execute("SELECT book_id FROM BookMetadata ORDER BY RANDOM() LIMIT 5").fetchall()
    # get 3 random songs from the SongMetadata table
    songs = con.execute("SELECT music_id FROM MusicMetadata ORDER BY RANDOM() LIMIT 3")

    # add them to the collection+metadata
    for book in books:
        con.execute("INSERT INTO Collections_Metadata (collection_id, book_id, music_id) VALUES (?, ?, Null)",
                    (2, book[0]))
    for song in songs:
        con.execute("INSERT INTO Collections_Metadata (collection_id, book_id, music_id) VALUES (?, Null, ?)",
                    (2, song[0]))

favoriteBooks()
neverRead()

con.commit()
