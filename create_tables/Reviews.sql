-- Destroy the Reviews table if it exists (this is just so we can cleanly -- rerun this file if we want to reset everything)
DROP TABLE IF EXISTS Reviews;

-- Create the Reviews table
CREATE TABLE Reviews
(   -- The review_id is the primary key for the Reviews table
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- The user that wrote the review
    user_id INTEGER NOT NULL,

    -- The title of the review
    title TEXT NOT NULL,

    -- The body of the review
    content TEXT NOT NULL,

    -- The rating of the review (0-5 stars)
    review TINYINT NOT NULL,

    -- The date the review was created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,

    -- An optional image for the review (ie screenshot)
    image_url text,

    FOREIGN KEY (review_id) REFERENCES Reviews(review_id)
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id)
);
