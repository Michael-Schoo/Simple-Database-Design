-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Collections_Reviews;

-- Create the Collections table
CREATE TABLE Collections_Reviews
(   collection_id INTEGER,
    review_id INTEGER,

    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id)
    FOREIGN KEY (review_id) REFERENCES Reviews(review_id)
    PRIMARY KEY (collection_id, review_id)
);
