import sqlite3
con = sqlite3.connect("../data.db")

# The users to add
data = [
    {'name': 'a', 'email': 'a@b.c'},
    {'name': 'Person', 'email': 'a@b.c', 'avatar': 'lol'},
    {'name': 'b', 'email': 'a@b.c', 'created': '2008-11-11 13:23:44'},
    {'name': 'a', 'email': 'l@b.c', 'created': '2008-11-11 13:23:44'},
    {'name': 'a', 'email': 'l@b.c', 'created': '2008-11-11 13:13:44', 'avatar': 'https://example.com/example.png'},
]


for row in data:
    # If there the created date is specified, use the provided date
    if ('created' in row):
        # add the user to the database
        con.execute("INSERT INTO Users (name, created_at, email, avatar_url) VALUES (?, ?, ?, ?)",
                    (row.get('name'), row.get('created', 'CURRENT_TIMESTAMP'), row.get('email'), row.get('avatar')))
    else:
        # add the user to the database
        con.execute("INSERT INTO Users (name, email, avatar_url) VALUES (?, ?, ?)",
                    (row.get('name'), row.get('email'), row.get('avatar')))

con.commit()
