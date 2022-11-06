-- Destroy the MusicMetadata table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS MusicMetadata;

-- Create the Collections table
CREATE TABLE MusicMetadata
(   -- The collection_id is the primary key for the MusicMetadata table
    music_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- The author of the music/song (if many artists then seperated by ',')
    artist TEXT NOT NULL,

    -- The title of the music/song
    title TEXT NOT NULL,

    -- an image of the music/song (image stored in Images table)
    image_id INTEGER,

    FOREIGN KEY (image_id) REFERENCES Images(image_id)
);

-- This table should contain every music/song someone could add to their collection
-- Only admins can add music/songs to this table (so that thay can be ensured it is good)
-- If a user wants to add a music/song to this list, they can request it to be added
