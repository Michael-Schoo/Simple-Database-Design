-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS CollectionMetadataBook;

-- Create the Collections table
CREATE TABLE CollectionMetadataBook
(   collection_metadata_book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection_id INTEGER NOT NULL,

    -- if many authors then seperated by ','
    authors TEXT NOT NULL,
    blurb TEXT NOT NULL,

    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id)
);
