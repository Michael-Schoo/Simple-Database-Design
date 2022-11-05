-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Collections_Images;

-- Create the Collections table
CREATE TABLE Collections_Images
(   collection_id INTEGER NOT NULL,
    image_id INTEGER NOT NULL,

    FOREIGN KEY (collection_id) REFERENCES Images(image_id)
    FOREIGN KEY (image_id) REFERENCES Collections(collection_id)
    PRIMARY KEY (image_id, collection_id)
);
