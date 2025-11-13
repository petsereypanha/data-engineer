
-- Create the films table based on CSV data structure
CREATE TABLE IF NOT EXISTS films (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year DECIMAL(6,1),
    country VARCHAR(100),
    duration DECIMAL(6,1),
    language VARCHAR(50),
    certification VARCHAR(50),
    gross DECIMAL(15,1),
    budget DECIMAL(15,1)
);

-- Load data using \copy (client-side command for Docker/psql)