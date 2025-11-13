-- Create the reviews table
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY,
    film_id INTEGER,
    num_user INTEGER,
    num_critic INTEGER,
    imdb_score REAL,
    num_votes INTEGER,
    facebook_likes INTEGER,
    FOREIGN KEY (film_id) REFERENCES films(id)
);