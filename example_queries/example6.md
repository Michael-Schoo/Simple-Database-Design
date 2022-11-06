# Example 5
> A person wants to customize their profile, and update a collection

Van Gogh (ID: 783) wants to customize their profile. They want to add the following information to their profile:
* name: `Van Gogh` from `User 783`
* profile picture: `https://van_gogh.com/me.jpg` from none
* email: `van_gogh@van_gogh.com` from `temp1b3bsn3@i_dont_care.io`
* wants to change created at date but can't

```sql
-- Update the user's information
UPDATE Users SET name = 'Van Gogh', email = 'van_gogh@van_gogh.com', avatar_url = 'https://van_gogh.com/me.jpg' WHERE user_id = 783;
```

They obviously want to see how their profile looks, so they go to the website and look at it.

```sql
-- Get the user's information
SELECT name, email, avatar_url FROM Users WHERE user_id = 783;

-- Get the user's collections
SELECT collection_id FROM Collections WHERE user_id = 783;

-- Does more things to get the collections
```

He decides that his collection of `Funny memes` is not funny enough, so he wants to add a new meme to it and change it's name:
* name: `Things I found` from `Funny memes`
* description: `Things I found on the internet` from `These are some funny memes`
* new meme:
  * song: `Never going to give you up` by `Rick Roll`
* and wants to add a new link: `Youtube` going to <https://www.youtube.com/watch?v=dQw4w9WgXcQ>

```sql
-- Update the collection's information
UPDATE Collections SET name = 'Things I found', description = 'Things I found on the internet' WHERE collection_id = 199;

-- Get the song id (id of 296)
SELECT song_id FROM Songs WHERE title = 'Never going to give you up';

-- Add the song to the collection
INSERT INTO Collections_Metadata VALUES(199, null, 296);

-- Make link (id of 92)
INSERT INTO Links VALUES(null, 'Youtube', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ');

-- Add the link to the collection
INSERT INTO Collections_Links VALUES(199, 92);
```
