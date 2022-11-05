-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS MusicMetadata;

-- Create the Collections table
CREATE TABLE MusicMetadata
(   music_metadata_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- if many artists then seperated by ','
    artist TEXT NOT NULL,
    title TEXT NOT NULL,
    image_id INTEGER,

    FOREIGN KEY (image_id) REFERENCES Images(image_id)
);
