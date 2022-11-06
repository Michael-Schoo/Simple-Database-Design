# Open database
import sqlite3
con = sqlite3.connect("../data.db")

# The list of sql commands and python files to execute
list = [
    "Users.py",
    "Users.sql",
    "Links.sql",
    "Images.sql",
    "random_books.py",
    "random_songs.py",
    "Collections.py",
]

# Execute each sql command
for file in list:
    print("file: "+file)

    # Open and read the file as a single buffer
    with open("../populate_db/"+file, 'r') as f:
        # depending on if it is sql or python, use the appropriate method to execute
        if (file.endswith(".py")):
            exec(f.read())
        elif (file.endswith(".sql")):
            con.executescript(f.read())
    print()

# Close database
con.commit()
con.close()