# Open database
import sqlite3
import pandas
con = sqlite3.connect("../data.db")
con.row_factory = sqlite3.Row

list = [
    "AllCollections.sql",
    "AllUsers.sql",
    "AllUsers (sorted).sql",
]


def dict_from_row(row):
    return dict(zip(row.keys(), row))


for file in list:
    print("file: "+file)
    
    with open("../example_queries/"+file, 'r') as f:
        # print(f.read())
        if (file.endswith(".py")):
            exec(f.read())
        elif (file.endswith(".sql")):
            data = [dict_from_row(row) for row in con.execute(f.read()).fetchall()]
            df = pandas.DataFrame.from_dict(data)
            print(df)

    print()

# Close database
con.commit()
con.close()

