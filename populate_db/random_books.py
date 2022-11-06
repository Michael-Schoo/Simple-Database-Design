# Api doc:
# https://bookstore.docs.apiary.io
import sqlite3
import requests

con = sqlite3.connect("../data.db")

# Get the books
def getBooks() -> list:
    headers = {
        "User-agent": "lol",
    }
    # request = requests.get("http://books.cloudfoundry.com/data/books", headers=headers)
    request = requests.get(
        "https://private-anon-2cbb16926a-bookstore.apiary-mock.com/data/books", headers=headers)

    books = request.json()
    return books


for i, book in enumerate(getBooks()):
    # Go through each book and add it to the database
    print(f"Added book {i+1}")
    title = book.get('title')
    author = book.get('author')
    summary = book.get('summary')
    image_url = book.get('image')
    price = book.get('price').get('value')

    # If there is an image, add it to the database
    image_id = None
    if image_url:
        con.execute("INSERT INTO Images (image_url, alt) VALUES (?, ?)",
                    (image_url, "Book image for "+title))
        image_id = con.execute("SELECT last_insert_rowid()").fetchone()[0]

    # Add the book to the database
    con.execute("INSERT INTO BookMetadata (title, author, price, summary, image_id) VALUES (?, ?, ?, ?, ?)",
                (title, author, price, summary, image_id))

con.commit()
