import pprint
import sqlite3
con = sqlite3.connect("../data.db")
con.row_factory = sqlite3.Row

# This file gets all collections and makes a dictionary with the metadata
# This could be used to display the contents of a collection

results = []

# Get all collections
collections = con.execute("SELECT collection_id, user_id, name, description, created_at FROM Collections").fetchall()

for collection in collections:
    result = {}
    result['collection_id'] = collection[0]
    # result['user_id'] = collection[1]
    result['name'] = collection[2]
    result['description'] = collection[3]
    result['created_at'] = collection[4]

    # get user from table
    user = con.execute(
        "SELECT user_id, name, created_at, email, avatar_url FROM Users WHERE user_id = ?", (collection[1],)).fetchone()
    result['user'] = {
        'user_id': user[0],
        'name': user[1],
        # 'created_at': user[2],
        # 'email': user[3],
        'avatar_url': user[4]
    }

    # Get all metadata for this collection
    metadata = con.execute(
        "SELECT collection_id, music_id, book_id FROM Collections_Metadata WHERE collection_id = ?", (collection[0],)).fetchall()
    result['items'] = []
    for item in metadata:
        if (item[2] != None):
            # get book metadata
            book = con.execute(
                "SELECT book_id, author, title, price, summary, image_id FROM BookMetadata WHERE book_id = ?", (item[2],)).fetchone()
            # get image url
            image = con.execute(
                "SELECT image_id, image_url FROM Images WHERE image_id = ?", (book[5],)).fetchone()
            result['items'].append({
                'type': 'book',
                'book_id': book[0],
                'author': book[1],
                'title': book[2],
                'price': book[3],
                'summary': book[4],
                # 'image_id': book[5],
                'image_url': image[1]
            })

        if (item[1] != None):
            # get music metadata
            music = con.execute(
                "SELECT music_id, artist, title, image_id FROM MusicMetadata WHERE music_id = ?", (item[1],)).fetchone()
            # get image url
            image = con.execute(
                "SELECT image_id, image_url FROM Images WHERE image_id = ?", (music[3],)).fetchone()
            result['items'].append({
                'type': 'music',
                'music_id': music[0],
                'artist': music[1],
                'title': music[2],
                # 'image_id': music[3],
                'image_url': image[1]
            })
    
    # get links
    links = con.execute("SELECT link_id FROM Collections_Links WHERE collection_id = ?", (collection[0],)).fetchall()
    result['links'] = []
    for link in links:
        link_info = con.execute("SELECT link_id, title, url, favicon_url FROM Links WHERE link_id = ?", (link[0],)).fetchone()
        result['links'].append({
            'link_id': link_info[0],
            'title': link_info[1],
            'url': link_info[2],
            'favicon_url': link_info[3]
        })

    # get images
    images = con.execute("SELECT image_id FROM Collections_Images WHERE collection_id = ?", (collection[0],)).fetchall()
    result['images'] = []
    for image in images:
        image_info = con.execute("SELECT image_id, image_url, alt FROM Images WHERE image_id = ?", (image[0],)).fetchone()
        result['images'].append({
            'image_id': image_info[0],
            'image_url': image_info[1],
            'alt': image_info[2]
        })


    results.append(result)
    print()

# format dict
print("Collections:")
pp = pprint.PrettyPrinter(indent=4)
# Not everything printed is visible in the console (because of max length)
pp.pprint(results)

# output's something like this:
# {
#     'collection_id': 2,
#     'created_at': '2022-11-05 03:37:25',
#     'description': 'The following art is horrible',
#     'items': [
#         {
#             'author': 'Terry Brooks',
#             'book_id': 3,
#             'image_url': 'http://s.s-bol.com/imgbase0/imagebase/large/FC/2/2/5/2/9200000002212522.jpg',
#             'price': 17.5,
#             'summary': 'Vijf eeuwen geleden werd de wereld door een ',
#             'title': 'Magic staff',
#             'type': 'book'
#         },
#         {
#             'artist': 'Malky',
#             'image_url': 'https://assets.genius.com/images/default_cover_image.png?1667505721',
#             'music_id': 3,
#             'title': 'Soon',
#             'type': 'music'
#         }
#     ],
#     'links': [
#         {
#             'favicon_url': 'https://www.google.com/s2/favicons?domain=www.google.com',
#             'link_id': 1,
#             'title': 'Google',
#             'url': 'https://www.google.com/' 
#         }
#     ],
#     'images': [
#         {
#             'alt': 'alt text',
#             'image_id': 1,
#             'image_url': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
#         }
#     ],
#     'name': 'Never read/listen to these',
#     'user': {
#         'avatar_url': 'https://example.com/example.png',', 
#         'name': 'Person', 'user_id': 4
#     }
# }
