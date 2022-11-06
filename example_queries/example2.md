## Example 2
> A user gets new items added to the collection options, and then makes a new collection with them.

In this example, there is already a user that has interacted with the website many times. The user is called **John Doe** (id: 582) and is a bit annoyed at the few selections for books and music. He contacts the owners, and they manually add the requested items to the database. The items are:
* a song called `Peppa Pic` by `someone`
  * image: `https://example.com/peppa_pic.jpg`
* a book called `The Hungry Caterpillar` by `Eric Carle`
  * no image
  * price of `$2.99`
  * summary: `a very good book`

```sql
-- Add the song image to the database (its id will be 121)
INSERT INTO Images VALUES(null, 'https://example.com/peppa_pic.jpg');

-- Add the song to the database (its id will be 343)
INSERT INTO MusicMetadata VALUES(null, 'someone', 'Peppa Pic', 121);

-- Add the book to the database (its id will be 296)
INSERT INTO BookMetadata VALUES(null, 'Eric Carle', 'The Hungry Caterpillar', 2.99, 'a very good book', null);
```

Now that the items are added, John Doe wants to add them to his collection. The collection is called `Questionable things`.

```sql
-- Search for the new items by name (the ids will be 343 and 296)
SELECT music_id FROM MusicMetadata WHERE title = 'Peppa Pic';
SELECT book_id FROM BookMetadata WHERE title = 'The Hungry Caterpillar';

-- Create the collection (its id will be 199)
INSERT INTO Collections VALUES(null, 582, 'Questionable things', 'A collection of questionable things', CURRENT_TIMESTAMP);

-- Add the items to the collection (book: 296, song: 343)
INSERT INTO Collections_Metadata VALUES(199, 343, null);
INSERT INTO Collections_Metadata VALUES(199, null, 296);
```
