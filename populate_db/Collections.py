import sqlite3
con = sqlite3.connect("../data.db")

data = [
    {'userId': 'a', 'name': '?', 'type': 'book', 'description': 'a', 'created': '2008-11-11 13:23:44'},
    {'userId': 'a', 'name': '?', 'type': 'book', 'description': 'a'},
]


for row in data:
    if ('created' in row):
        con.execute("INSERT INTO Collections (UserID, Name, Type, Description, CreatedAt) VALUES (?, ?, ?, ?, ?)",
                    (row['userId'], row['name'], row['type'], row['description'], row['created']))
    else:
        con.execute("INSERT INTO Collections (UserID, Name, Type, Description) VALUES (?, ?, ?, ?)",
                    (row['userId'], row['name'], row['type'], row['description']))

con.commit()
