-- Create the people table
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    birthdate DATE,
    deathdate DATE
);
