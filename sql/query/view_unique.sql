-- Your code to create the view:
CREATE VIEW library_authors AS
SELECT DISTINCT author AS unique_author
FROM books;

-- Select all columns from library_authors
SELECT * FROM library_authors

-- Select the first 10 genres from books using PostgreSQL
SELECT genre
FROM books
LIMIT 10;