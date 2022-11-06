-- Destroy the Users table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Users;

-- Create the Users table
CREATE TABLE Users
(   -- The user_id is the primary key for the Users table
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    -- The username of the user
    name TEXT NOT NULL,

    -- The time the user was created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- The email of the user
    email TEXT NOT NULL,

    -- The optional custom avatar image for the user
    avatar_url TEXT
);

-- This table is for storing users
-- Users can create and modify themselves
-- The created_at field is automatically set to the current time when the user is created
