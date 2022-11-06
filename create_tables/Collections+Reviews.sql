-- Destroy the Collections_Reviews table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Collections_Reviews;

-- Create the Collections table
CREATE TABLE Collections_Reviews
(   -- The collection_id is the primary key for the Collections_Reviews table
    collection_id INTEGER,

    -- The review_id also is the primary key for the Collections_Reviews table
    review_id INTEGER,

    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id)
    FOREIGN KEY (review_id) REFERENCES Reviews(review_id)
    PRIMARY KEY (collection_id, review_id)
);
