import sqlite3
con = sqlite3.connect("../data.db")

data = [
    {'name': 'a', 'description': 1},
    {'name': 'b', 'description': "lol"},
]

for row in data:
    con.execute("INSERT INTO B (name, description) VALUES (?, ?)", (row['name'], row['description']))

con.commit()