-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Collections_Metadata;

-- Create the Collections table
CREATE TABLE Collections_Metadata
(   -- The collection_id is the primary key for the Collections table
    collection_id INTEGER NOT NULL,

    -- Second primary key only going to one of the below (not both, or none) 
    music_id INTEGER,
    book_id INTEGER,

    FOREIGN KEY (collection_id) REFERENCES Images(image_id)
    FOREIGN KEY (music_id) REFERENCES MusicMetadata(music_id)
    FOREIGN KEY (book_id) REFERENCES BookMetadata(book_id)
    PRIMARY KEY (collection_id, music_id, book_id)
);

-- Joining table for the Collections and MusicMetadata/BookMetadata tables