## Example 1
> A user create an account, makes a collection, and shares it to a friend.

Lets imagine that an new user visits our website, and wants to create an account. His personal information is:
* Name: `John Doe`
* Email: `john.doe@gmail.com`
* Custom avatar: `https://example.com/john_doe.jpg`

```sql
-- Create a new user (its id will be 582)
INSERT INTO Users VALUES(null, 'John Doe', CURRENT_TIMESTAMP, 'john.doe@gmail.com', 'https://example.com/john_doe.jpg');
```

Now that they have an account, they want to create a new collection. The collection will have the following information:
* Name: `My memories`
* Description: `A collection of songs that remind me of my childhood`
* The things added to the collection are:
  * a song called `The Final Countdown` by `Europe` (ID: 342)
  * a book called `The Lord of the Rings` by `J.R.R. Tolkien` (ID: 295)

```sql
-- Create the collection (its id will be 64)
INSERT INTO Collections VALUES(null, 'My memories', 'A collection of songs that remind me of my childhood', 1, CURRENT_TIMESTAMP);

-- Find the book and song from name (the ids will be 342 and 295)
SELECT book_id FROM BookMetadata WHERE title = 'The Lord of the Rings' AND author = 'J.R.R. Tolkien';
SELECT music_id FROM MusicMetadata WHERE title = 'The Final Countdown' AND artist = 'Europe';

-- Add the items to the collection
INSERT INTO Collections_Metadata VALUES(64, 342, null);
INSERT INTO Collections_Metadata VALUES(64, null, 295);
```

Now that the collection is created, the user wants share it with their friends. Their friend **Jane Doe** opens the website and wants to see the collection. She searches for the collection by name, and finds it. *(in [`GetCollectionsWithMetadata.py`](./GetCollectionsWithMetadata.py) has a better method)*

```sql
-- Search for the collection by name (the id will be 64)
SELECT collection_id FROM Collections WHERE name = 'My memories';

-- Get the collection's information
SELECT user_id, name, description, created_at FROM Collections WHERE collection_id = 64;

-- Get the user's information (to show the avatar and name of author, id of 582)
SELECT name as user_name, avatar_url FROM Users WHERE user_id = 582;

-- REPEAT below many times because there can be many items
-- Get the items in the collection
SELECT music_id, book_id FROM Collections_Metadata WHERE  collection_id = 64;

-- If the item is a music, get its information (id of 342)
SELECT artist, title, image_id FROM MusicMetadata WHERE music_id = 342;

-- If the item is a book, get its information (id of 295)
SELECT author, title, price, summary, image_id FROM BookMetadata WHERE book_id = 295;

-- Get the image of the item (id of 102 and 95)
SELECT image_id, image_url FROM Images WHERE image_id = 102
SELECT image_id, image_url FROM Images WHERE image_id = 95

-- Then show to user
```

This friend loves the collection, and wants to comment on it. They first have to create an account, and then they can comment on the collection. Information about the comment is:
* Comment title: `This is a great collection!`
* Comment body: `I love the songs and the book! It reminds me of my childhood too!`
* Rating: `5 stars`
* Collection: `My memories` (ID: 64)
* No image provided
* User:
  * Name: `Jane Doe`
  * Email: `10@minutemail.com`
  * No avatar


```sql
-- Create a new user (its id will be 583)
INSERT INTO Users VALUES(null, 'Jane Doe', CURRENT_TIMESTAMP, '10@minutemail.com', null);

-- Create the comment (its id will be 826)
INSERT INTO Reviews VALUES(null, 583, 'This is a great collection!', 'I love the songs and the book! It reminds me of my childhood too!', 5, CURRENT_TIMESTAMP, null);

-- Add to joining table
INSERT INTO Collections_Reviews VALUES(64, 826);
```

After some time the user wants to see the comments on the collection. They refresh the page, and the comments are shown.

```sql
-- Get the comments on the collection (id of 64) 
SELECT review_id FROM Collections_Reviews WHERE collection_id = 64;

-- Get the information about the review (id of 826)
SELECT user_id, title, body, created_at, image_url FROM Reviews WHERE review_id = 826;

-- Get the user's information (id of 583 and more for other users)
SELECT name as user_name, avatar_url FROM Users WHERE user_id = 583;
```

The user likes the many comments, but they want to see the comments sorted by rating. They click on the rating column, and the comments are sorted by rating. They especially want to know why some people don't like it.

```sql
-- Get the comments on the collection (id of 64)
SELECT review_id FROM Collections_Reviews WHERE collection_id = 64;

-- Get the information about the review (id of 826)
SELECT user_id, title, body, created_at, image_url FROM Reviews WHERE review_id = 826 ORDER BY rating DESC;

-- Get the user's information (id of 583 and more for other users)
SELECT name as user_name, avatar_url FROM Users WHERE user_id = 583;
```
