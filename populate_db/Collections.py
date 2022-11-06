import sqlite3
con = sqlite3.connect("../data.db")

# The collections to add
data = [
    {'user_id': 1, 'name': 'My favorite books', 'description': 'Books that you should read, because I say so', 'created': '2008-11-11 13:23:44'},
    {'user_id': 4, 'name': 'Never read/listen to these', 'description': 'The following art is horrible'},
    {'user_id': 2, 'name': 'Books for life', 'description': 'Books and images'},
]


for row in data:
    # If there the created date is specified, use the provided date
    if ('created' in row):
        # add the collection to the database
        con.execute("INSERT INTO Collections (user_id, name, description, created_at) VALUES (?, ?, ?, ?)",
                    (row.get('user_id'), row.get('name'), row.get('description'), row.get('created')))
    else:
        # add the collection to the database
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

def imageAndLinks():
    # get 1 random books from the BookMetadata table
    books = con.execute("SELECT book_id FROM BookMetadata ORDER BY RANDOM() LIMIT 1").fetchall()

    # add them to the collection+metadata
    for book in books:
        con.execute("INSERT INTO Collections_Metadata (collection_id, book_id) VALUES (?, ?)",
                    (3, book[0]))
    
    # get a random image
    image = con.execute("SELECT image_id FROM Images ORDER BY RANDOM() LIMIT 1").fetchone()
    # add it to the collection
    con.execute(
        "INSERT OR IGNORE INTO Collections_Images (collection_id, image_id) VALUES (?, ?)", (3, image[0]))

    # get random link
    link = con.execute("SELECT link_id FROM Links ORDER BY RANDOM() LIMIT 1").fetchone()
    # add it to the collection
    con.execute(
        "INSERT OR IGNORE INTO Collections_Links (collection_id, link_id) VALUES (?, ?)", (3, link[0]))


favoriteBooks()
neverRead()
imageAndLinks()

con.commit()
