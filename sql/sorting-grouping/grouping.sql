-- Find the release_year and film_count of each year
SELECT release_year, COUNT(*) AS film_count
FROM films
GROUP BY release_year
ORDER BY release_year ASC;

-- Find the release_year and average duration of films for each year
SELECT release_year, AVG(duration) AS avg_duration
FROM films
GROUP BY release_year
ORDER BY release_year ASC;

-- Find the release_year, country, and max_budget, then group and order by release_year and country
SELECT release_year, country, MAX(budget) AS max_budget
FROM films
GROUP BY release_year, country
ORDER BY release_year ASC, country ASC;

-- Find the release_year with the highest number of distinct languages
SELECT
  release_year,
  COUNT(DISTINCT language) AS language_diversity_count
FROM
  films
GROUP BY
  release_year
ORDER BY
  language_diversity_count DESC
LIMIT 1;

-- Select the country and distinct count of certification as certification_count
SELECT country, COUNT(DISTINCT certification) AS certification_count 
FROM films
-- Group by country
GROUP BY country
-- Filter results to countries with more than 10 different certifications
HAVING COUNT(DISTINCT certification) > 10;

-- Select the country and average_budget from films
SELECT country, AVG(budget) AS average_budget
FROM films
-- Group by country
GROUP BY country
-- Filter to countries with an average_budget of more than one billion
HAVING AVG(budget) > 1000000000
-- Order by descending order of the aggregated budget
ORDER BY average_budget DESC;

-- Select the release_year for films released after 1990 grouped by year
SELECT release_year, COUNT(*) AS film_count
FROM films
WHERE release_year > 1990
GROUP BY release_year
ORDER BY film_count DESC;

-- Modify the query to also list the average budget and average gross
SELECT release_year, AVG(budget) AS average_budget, AVG(gross) AS average_gross
FROM films
WHERE release_year > 1990
GROUP BY release_year;

SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
WHERE release_year > 1990
GROUP BY release_year
-- Modify the query to see only years with an avg_budget of more than 60 million
HAVING AVG(budget) > 60000000;

SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
WHERE release_year > 1990
GROUP BY release_year
HAVING AVG(budget) > 60000000
-- Order the results from highest to lowest average gross and limit to one
ORDER BY AVG(gross) DESC
LIMIT 1;