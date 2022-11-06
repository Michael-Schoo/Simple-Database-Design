-- For example, when a user creates a collection, the collection's information is added to the database (note: the 1 is the user's ID). 
INSERT INTO Collections VALUES(null, 1, 'Collection Name', 'Collection Description', CURRENT_TIMESTAMP);

-- Select that data
SELECT * FROM Collections WHERE collection_id = last_insert_rowid();
