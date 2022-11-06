# Open database
import sqlite3
con = sqlite3.connect("../data.db")

# The list of sql commands to execute
list = [
    "Users.sql",
    "Collections.sql",
    "Images.sql",
    "Links.sql",
    "Collections+Images.sql",
    "Collections+Links.sql",
    "Collections+Reviews.sql",
    "BookMetadata.sql",
    "MusicMetadata.sql",
    "Collections+Metadata.sql",
]

# Execute each sql command
for file in list:
    print("file: "+file)
   
    # Open and read the file as a single buffer
    with open("../create_tables/"+file, 'r') as f:
        # depending on if it is sql or python, use the appropriate method to execute
        if (file.endswith(".py")):
            exec(f.read())
        elif (file.endswith(".sql")):
            con.executescript(f.read())
    print()

# Close database
con.commit()
con.close()
