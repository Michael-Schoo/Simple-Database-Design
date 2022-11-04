import sqlite3
con = sqlite3.connect("../data.db")

data = [
    {'user_id': 'a', 'name': '?', 'type': 'book', 'description': 'a', 'created': '2008-11-11 13:23:44'},
    {'user_id': 'a', 'name': '?', 'type': 'book', 'description': 'a'},
]


for row in data:
    # if ('created' in row):
    #     con.execute("INSERT INTO Collections (user_id, name, type, description, created_at) VALUES (?, ?, ?, ?, ?)",
    #                 (row['user_id'], row['name'], row['type'], row['description'], row['created']))
    # else:
    con.execute("INSERT INTO Collections (user_id, name, type, description) VALUES (?, ?, ?, ?)",
                (row.get('user_id'), row.get('name'), row.get('type'), row.get('description')))

con.commit()
