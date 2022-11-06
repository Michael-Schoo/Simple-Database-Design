-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Images;

-- Create the Collections table
CREATE TABLE Images
(   -- The image_id is the primary key for the Images table
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- The url for the image
    image_url TEXT NOT NULL,

    -- The alternative text (if aplicable)
    alt TEXT
);

-- This table is for storing images
-- currently only an admin can add images to the database
-- Users can only use images that are already exit
