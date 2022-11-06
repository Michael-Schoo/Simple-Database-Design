-- Destroy the Collections_links table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Collections_links;

-- Create the Collections_links table
CREATE TABLE Collections_links
(   -- The collection_id is the primary key for the Collections_links table
    collection_id INTEGER NOT NULL,

    -- The link_id also is the primary key for the Collections_links table
    link_id INTEGER NOT NULL,

    FOREIGN KEY (collection_id) REFERENCES Links(link_id)
    FOREIGN KEY (link_id) REFERENCES Collections(collection_id)
    PRIMARY KEY (link_id, collection_id)
);

-- Joining table for the Collections and Links tables
