-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS BookMetadata;

-- Create the Collections table
CREATE TABLE BookMetadata
(   book_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- if many authors then seperated by ','
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    price INTEGER NOT NULL,
    summary TEXT NOT NULL,
    image_id INTEGER,

    FOREIGN KEY (image_id) REFERENCES Images(image_id)
);
