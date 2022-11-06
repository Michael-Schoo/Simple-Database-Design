-- Destroy the Links table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Links;

-- Create the Links table
CREATE TABLE Links
(   -- The link_id is the primary key for the Links table
    link_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- The title of the link
    title TEXT NOT NULL,

    -- The url for the link
    url TEXT NOT NULL,

    -- The favicon of the link's website (if aplicable)
    favicon_url TEXT
);
