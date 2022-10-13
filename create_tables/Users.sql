-- Destroy the Users table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Users;

-- Create the Users table
CREATE TABLE Users
(   ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    Email TEXT NOT NULL,
    AvatarURL TEXT
);
