-- Destroy the Collections_Images table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Collections_Images;

-- Create the Collections_Images table
CREATE TABLE Collections_Images
(   -- The collection_id is the primary key for the Collections_Images table
    collection_id INTEGER NOT NULL,

    -- The image_id also is the primary key for the Collections_Images table
    -- Note the user can't add any new images (unless they contact support), this to ensure the images are aproved
    image_id INTEGER NOT NULL,

    FOREIGN KEY (collection_id) REFERENCES Images(image_id)
    FOREIGN KEY (image_id) REFERENCES Collections(collection_id)
    PRIMARY KEY (image_id, collection_id)
);
