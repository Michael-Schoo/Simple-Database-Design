# Example 3
> A user no longer wants to see an item in their collection, and then desists to delete account.

Jane Smith (id: 102) is a user who has been semi active on the website for a while. She has a collection called `My favorite books` (id: 43), but she no longer wants to see the book `The Lord of the Rings` (id: 295) in her collection.
    
```sql
-- Get the collection id (id of 43)
SELECT collection_id FROM Collections WHERE name = 'My favorite books' AND user_id = 102;

-- Remove the item from the collection
DELETE FROM Collections_Metadata WHERE collection_id = 43 AND book_id = 295;
```

Jane Smith is now unhappy with the website, and wants to delete her account. She has to delete all of her collections, and then delete her account.

```sql
-- Get the collection ids (ids of 43 and more)
SELECT collection_id FROM Collections WHERE user_id = 102;

-- Delete all of the items in the collections (many times repeated)
DELETE FROM Collections_Metadata WHERE collection_id = 43;

-- Delete all of the collections and their reviews (many times repeated)
-- Get the collection ids (43 and more)
SELECT collection_id FROM Collections WHERE user_id = 102;
DELETE FROM Collections WHERE collection_id = 43;
DELETE FROM Collections_Reviews WHERE collection_id = 43
DELETE FROM Reviews WHERE collection_id = 43

-- Delete the reviews made my them (many times repeated)
-- Get the review ids (ids of 736 and more)
SELECT review_id FROM Reviews WHERE user_id = 102;
DELETE FROM Collections_Reviews WHERE review_id = 736;
DELETE FROM Reviews WHERE review_id = 736;

-- Finally, delete the user
DELETE FROM Users WHERE user_id = 102;
```
