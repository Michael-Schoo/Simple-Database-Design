import sqlite3
con = sqlite3.connect("../data.db")

data = [
    {'name': 'a', 'email': 'a@b.c'},
    {'name': 'Person', 'email': 'a@b.c', 'avatar': 'lol'},
    {'name': 'b', 'email': 'a@b.c', 'created': '2008-11-11 13:23:44'},
    {'name': 'a', 'email': 'l@b.c', 'created': '2008-11-11 13:23:44'},
    {'name': 'a', 'email': 'l@b.c', 'created': '2008-11-11 13:13:44', 'avatar': 'https://example.com/example.png'},
]


for row in data:
    if ('created' in row):
        con.execute("INSERT INTO Users (name, created_at, email, avatar_url) VALUES (?, ?, ?, ?)",
                    (row.get('name'), row.get('created', 'CURRENT_TIMESTAMP'), row.get('email'), row.get('avatar')))
    else:
        con.execute("INSERT INTO Users (name, email, avatar_url) VALUES (?, ?, ?)",
                    (row.get('name'), row.get('email'), row.get('avatar')))

con.commit()
