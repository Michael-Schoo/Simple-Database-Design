-- For example, when the sign up form is submitted, the user's information is added to the database. (note: the passwords woule be set up into another table - with more security)
INSERT INTO Users VALUES(null, 'Username', CURRENT_TIMESTAMP, 'their@email.com', 'https://their.avatar.com');

-- Select that data
SELECT * FROM Users WHERE user_id = last_insert_rowid();
