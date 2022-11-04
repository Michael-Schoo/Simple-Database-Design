-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS CollectinImageGalery;

-- Create the Collections table
CREATE TABLE CollectinImageGalery
(   collection_image_galery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    alt TEXT NOT NULL,

    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id)
);
