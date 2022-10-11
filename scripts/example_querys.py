# Open database
import sqlite3
con = sqlite3.connect("../data.db")

list = [
    "a.sql",
    "b.sql",
]

for file in list:
    print("file: "+file)
    
    with open("../example_querys/"+file, 'r') as f:
        # print(f.read())
        if (file.endswith(".py")):
            exec(f.read())
        elif (file.endswith(".sql")):
            print(con.execute(f.read()).fetchall())
    print()

# Close database
con.commit()
con.close()