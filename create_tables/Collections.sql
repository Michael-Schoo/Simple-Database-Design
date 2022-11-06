-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Collections;

-- Create the Collections table
CREATE TABLE Collections
(   -- The collection_id is the primary key for the Collections table
    collection_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- The user who created the collection
    user_id INTEGER NOT NULL,

    -- The name of the collection
    name TEXT NOT NULL,

    -- The description of the collection
    description TEXT NOT NULL,

    -- The date the collection was created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,

    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
