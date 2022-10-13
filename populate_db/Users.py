import sqlite3
con = sqlite3.connect("../data.db")

data = [
    {'name': 'a', 'email': 'a@b.c'},
    {'name': 'b', 'email': 'a@b.c', 'avatar': 'lol'},
    {'name': 'b', 'email': 'a@b.c', 'created': '2008-11-11 13:23:44'},
    {'name': 'a', 'email': 'l@b.c', 'created': '2008-11-11 13:23:44'},
    {'name': 'a', 'email': 'l@b.c', 'created': '2008-11-11 13:13:44', 'avatar': 'https://'},
]


for row in data:
    if ('avatar' not in row):
        row['avatar'] = None

    if ('created' in row):
        con.execute("INSERT INTO Users (Name, CreatedAt, Email, AvatarURL) VALUES (?, ?, ?, ?)", (row['name'], row['created'], row['email'], row['avatar']))
    else:
        con.execute("INSERT INTO Users (Name, Email, AvatarURL) VALUES (?, ?, ?)", (row['name'], row['email'], row['avatar']))

con.commit()
