# Open database
import sqlite3
con = sqlite3.connect("../data.db")

list = [
    "Users.sql",
    "Collections.sql",
    "Images.sql",
    "Links.sql",
    "Collections+Images.sql",
    "Collections+Links.sql",
    "Collections+Reviews.sql",
    "CollectionMetadata (book).sql",
    "CollectionMetadata (music).sql",
]

for file in list:
    print("file: "+file)
   
    with open("../create_tables/"+file, 'r') as f:
        # print(f.read())
        if (file.endswith(".py")):
            exec(f.read())
        elif (file.endswith(".sql")):
            con.executescript(f.read())
    print()

# Close database
con.commit()
con.close()
