-- Destroy the Teachers table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS A;
-- Create the teachers table
CREATE TABLE A
(   ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Description TEXT
);
