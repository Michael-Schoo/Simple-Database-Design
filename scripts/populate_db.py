# Open database
import sqlite3
con = sqlite3.connect("../data.db")

list = [
    "Users.py",
    "Users.sql",
    "Collections.py",
    "random_songs.py",
    "random_books.py",
]

for file in list:
    print("file: "+file)
    with open("../populate_db/"+file, 'r') as f:
        # print(f.read())
        if (file.endswith(".py")):
            exec(f.read())
        elif (file.endswith(".sql")):
            con.executescript(f.read())
    print()

# Close database
con.commit()
con.close()