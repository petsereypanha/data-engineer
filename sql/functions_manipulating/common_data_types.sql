 -- Select all columns from the TABLES system database
 SELECT * 
 FROM information_schema.tables
 -- Filter by schema
 WHERE table_schema = 'public';


 -- Select all columns from the COLUMNS system database
 SELECT * 
 FROM information_schema.columns 
 WHERE table_name = 'actor';


-- Get the column name and data type
SELECT
 	column_name, 
    data_type
-- From the system database information schema
FROM information_schema.COLUMNS 
-- For the customer table
WHERE table_name = 'customer';


SELECT
 	-- Select the rental and return dates
	    rental_date,
        return_date,
 	-- Calculate the expected_return_date
	    rental_date + INTERVAL '3 days' AS expected_return_date
FROM rental;


-- Select the title and special features column 
SELECT 
  title, 
  special_features 
FROM film;


-- Select the title and special features column 
SELECT 
  title, 
  special_features 
FROM film
-- Use the array index of the special_features column
WHERE special_features[1] = 'Trailers';


-- Select the title and special features column 
SELECT 
  title, 
  special_features 
FROM film
-- Use the array index of the special_features column
WHERE special_features[2] = 'Deleted Scenes';


SELECT
  title, 
  special_features 
FROM film 
-- Modify the query to use the ANY function 
WHERE 'Trailers' = ANY (special_features);


SELECT 
  title, 
  special_features 
FROM film 
-- Filter where special_features contains 'Deleted Scenes'
WHERE special_features @> ARRAY['Deleted Scenes'];


