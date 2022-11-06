# Example 4
> A technological person wants to make a fancy collection.

Joe Bloggs (ID: 582), a computer geek, wants to make the best collection on the website. He notices that few people add links and other images to their collections. He wants to add the following information to his collection:
* name: `Best collection`
* description: `The best collection on the website (and my favorite books)`
* books:
  * `SQL for Dummies` by `person') drop table users;--` (id: 296)
  * `How to make a website` by `Joe Bloggs` (id: 263)
* images carousel:
  * `https://example.com/cool_image.jpg` (id: 121)
  * `https://example.com/cool_image2.jpg` (id: 122)
* links
  * URL: `https://github.com/joe-bloggs/`, text: `Joe's Github`, favicon: `https://github.com/favicon.ico`
  

```sql
-- Get the book ids (ids of 296 and 263)
SELECT book_id FROM BookMetadata WHERE title = 'SQL for Dummies';
SELECT book_id FROM BookMetadata WHERE title = 'How to make a website';

-- Create the collection (id of 199)
INSERT INTO Collections VALUES(null, 582, 'Best collection', 'The best collection on the website (and my favorite books)', CURRENT_TIMESTAMP);

-- Add the books to the collection (book: 296, book: 263)
INSERT INTO Collections_Metadata VALUES(199, null, 296);
INSERT INTO Collections_Metadata VALUES(199, null, 263);

-- Find the image ids (ids of 121 and 122)
-- Luckily they are already in the database
SELECT image_id FROM Images WHERE url = 'https://example.com/cool_image.jpg';
SELECT image_id FROM Images WHERE url = 'https://example.com/cool_image2.jpg';

-- Add the images to the database (ids of 121 and 122)
INSERT INTO Collections_Images VALUES(199, 121);
INSERT INTO Collections_Images VALUES(199, 122);

-- Add the link to the database (id of 24)
INSERT INTO Links VALUES(null, 'Joe''s Github', 'https://github.com/joe-bloggs', 'https://github.com/favicon.ico');

-- Add to join table
INSERT INTO Collections_links VALUES(199, 24)
```

He obviously wants to see how his collection looks, so he goes to the website and looks at it.

```sql
-- Get the collection's information
SELECT user_id, name, description, created_at FROM Collections WHERE collection_id = 199;

-- Get the user's information (to show the avatar and name of author, id of 24)
SELECT name as user_name, avatar_url FROM Users WHERE user_id = 24;

-- REPEAT below many times because there can be many items
-- Get the items in the collection
SELECT book_id FROM Collections_Metadata WHERE  collection_id = 199;

-- If the item is a book, get its information (id of 296 and 263)
SELECT author, title, price, summary, image_id FROM BookMetadata WHERE book_id = 296;
SELECT author, title, price, summary, image_id FROM BookMetadata WHERE book_id = 263;

-- Get the image of the item (id of 102 and 95)
SELECT image_id, image_url FROM Images WHERE image_id = 102
SELECT image_id, image_url FROM Images WHERE image_id = 95

-- REPEAT below many times because there can be many links and images
-- Get the links in the collection (id of 24)
SELECT link_id FROM Collections_links WHERE collection_id = 199;
SELECT text, url, favicon_url FROM Links WHERE link_id = 24;

-- Get the images in the collection (id of 121 and 122)
SELECT image_id FROM Collections_Images WHERE collection_id = 199;
SELECT image_id, image_url FROM Images WHERE image_id = 121;
SELECT image_id, image_url FROM Images WHERE image_id = 122;

-- Then show to user
```
