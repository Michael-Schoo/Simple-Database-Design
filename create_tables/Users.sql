-- Destroy the Users table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Users;

-- Create the Users table
CREATE TABLE Users
(   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    email TEXT NOT NULL,
    avatar_url TEXT
);
