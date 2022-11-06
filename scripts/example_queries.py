# Open database
import sqlite3
import pandas
con = sqlite3.connect("../data.db")
con.row_factory = sqlite3.Row

# The list of sql commands and python files to execute
list = [
    "GetCollectionsWithMetadata.py",
    "AllCollections.sql",
    "AllUsers.sql",
    "AllUsers (sorted).sql",
    "AllMusic.sql",
    "AllBooks.sql",
    "AllImages.sql",
    "AllCollection_Metadata.sql",
    "AddUser.m.sql"
]


def dict_from_row(row):
    # this function is used to convert a pandas row to a dictionary
    return dict(zip(row.keys(), row))

# Execute each sql command
for file in list:
    print("file: "+file)

    # Open and read the file as a single buffer
    with open("../example_queries/"+file, 'r') as f:
        # depending on if it is sql or python, use the appropriate method to execute
        if (file.endswith(".py")):
            exec(f.read())
        elif (file.endswith(".m.sql")):
            # This is used for multi-line sql commands
            print(con.executescript(f.read()).fetchall())
        elif (file.endswith(".sql")):
            # Get the sql result as a pandas dataframe (because looks better)
            data = [dict_from_row(row) for row in con.execute(f.read()).fetchall()]
            df = pandas.DataFrame.from_dict(data)
            print(df)

    print()

# Close database
con.commit()
con.close()
