-- For example, when a user creates a collection, the collection's information is added to the database (note: the 1 is the user's ID). 
INSERT INTO Reviews VALUES(null, 1, 'Collection Name', 'Collection Description', CURRENT_TIMESTAMP);

-- Select that data
SELECT * FROM Reviews WHERE review_id = last_insert_rowid();
