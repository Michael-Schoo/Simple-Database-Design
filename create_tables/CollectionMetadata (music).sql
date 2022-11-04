-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS CollectionMetadataMusic;

-- Create the Collections table
CREATE TABLE CollectionMetadataMusic
(   collection_metadata_music_id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection_id INTEGER NOT NULL,

    -- if many atrists then seperated by ','
    artist TEXT NOT NULL,

    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id)
);
