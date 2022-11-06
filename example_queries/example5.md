# Example 5
> A user is trying to find a collection (many different filters)

Sam Rock is a user who has been on competitors website and is seeing if this website is the best one. He is trying to find a collection that has a specific item in it. He wants to find a collection that has the book `The Lord of the Rings` (id: 295) in it.

```sql
-- Search bookmetadata for the book (id of 295)
SELECT book_id FROM BookMetadata WHERE title = 'The Lord of the Rings';

-- Search collections_metadata for the book (ids of 43 and 199)
SELECT collection_id FROM Collections_Metadata WHERE book_id = 295;

-- Get the collection name (ids of 43 and more)
SELECT collection_name FROM Collections WHERE collection_id = 43 OR collection_id = 199;
```

He likes the sound of the collection `My favorite books` (id: 43), but he wants to see if there are any other collections that were made before 2021

```sql
-- Get the collection name (ids of 43 and more)
SELECT collection_name FROM Collections WHERE created_at < 2021-01-01 AND (collection_id = 43 OR collection_id = 199 );
```

He likes the new options, but he wants to see if there are any collections that have more than 10 items in them.

```sql
-- Get the collection name (ids of 43 and more)
SELECT collection_name FROM Collections WHERE created_at < 2021-01-01 AND (collection_id = 43 OR collection_id = 199 );

-- Use collections_metadata to get the number of items in the collection (ids of 43 and 199)
SELECT collection_id FROM Collections_Metadata WHERE collection_id = 43 OR collection_id = 199 GROUP BY collection_id;

-- use the amount of items to filter the collections
```

After doing his research, he decides that this is the best website, because he found the best collections.