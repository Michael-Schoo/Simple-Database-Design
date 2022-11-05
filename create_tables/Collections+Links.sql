-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Collections_links;

-- Create the Collections table
CREATE TABLE Collections_links
(   collection_id INTEGER NOT NULL,
    link_id INTEGER NOT NULL,

    FOREIGN KEY (collection_id) REFERENCES Links(link_id)
    FOREIGN KEY (link_id) REFERENCES Collections(collection_id)
    PRIMARY KEY (link_id, collection_id)
);
