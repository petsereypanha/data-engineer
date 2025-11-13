-- Create the roles table
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY,
    film_id INTEGER,
    person_id INTEGER,
    role VARCHAR(50),
    FOREIGN KEY (film_id) REFERENCES films(id),
    FOREIGN KEY (person_id) REFERENCES people(id)
);
