-- Destroy the BookMetadata table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS BookMetadata;

-- Create the BookMetadata table
CREATE TABLE BookMetadata
(   -- The book_id is the primary key for the BookMetadata table
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- The author of the book (if many authors then seperated by ',')
    author TEXT NOT NULL,

    -- The title of the book
    title TEXT NOT NULL,

    -- The price of the book
    price INTEGER NOT NULL,

    -- the basic summary of the book
    summary TEXT NOT NULL,

    -- an image of the book (image stored in Images table)
    image_id INTEGER,

    FOREIGN KEY (image_id) REFERENCES Images(image_id)
);

-- This table should contain every book someone could add to their collection
-- Only admins can add books to this table (so that thay can be ensured it is good)
-- If a user wants to add a book to this list, they can request it to be added
