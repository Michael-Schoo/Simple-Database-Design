-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS CollectionLinks;

-- Create the Collections table
CREATE TABLE CollectionLinks
(   collection_link_id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    favicon_url TEXT,

    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id)
);
