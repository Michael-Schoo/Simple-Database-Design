-- Destroy the Collections table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Reviews;

-- Create the Collections table
CREATE TABLE Reviews
(   review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    review TINYINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    image_url text,

    FOREIGN KEY (review_id) REFERENCES Reviews(review_id)
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
