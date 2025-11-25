-- Count the number of null values in the ticker column
SELECT count(*) - count(ticker) AS missing
  FROM fortune500;


-- Count the number of null values in the industry column
SELECT count(*) - count(industry) AS missing
  FROM fortune500;


SELECT company.name
-- Table(s) to select from
  FROM company
       INNER JOIN fortune500
        ON company.ticker=fortune500.ticker;


-- Count the number of tags with each type
SELECT tag_type.type, count(*) as count
  FROM tag_type
 -- To get the count for each type, what do you need to do?
 GROUP BY tag_type.type
 -- Order the results with the most common tag types listed first
 ORDER BY count(*) DESC;

 

 -- Select the 3 columns desired
SELECT company.name, tag_type.tag, tag_type.type
  FROM company
  	   -- Join to the tag_company table
      INNER JOIN tag_company
      ON company.ticker = tag_company.ticker
       -- Join to the tag_type table
       INNER JOIN tag_type
      ON tag_company.tag_id = tag_type.tag_id
  -- Filter to most common type
  WHERE type='cloud';


-- Use coalesce
SELECT coalesce(industry, industry, 'Unknown') AS industry2,
       -- Don't forget to count!
      count(*) AS count
  FROM fortune500 
-- Group by what? (What are you counting by?)
 GROUP BY industry2
-- Order results to see most common first
 ORDER BY count DESC
-- Limit results to get just the one value you want
 LIMIT 1;

 
 -- Select the original value
SELECT profits_change, 
	   -- Cast profits_change
       CAST(profits_change AS integer)AS profits_change_int
  FROM fortune500;


-- Divide 10 by 3
SELECT 10/3, 
       -- Cast 10 as numeric and divide by 3
       10::numeric/3;


SELECT '3.2'::numeric,
       '-123'::numeric,
       '1e3'::numeric,
       '1e-3'::numeric,
       '02314'::numeric,
       '0002'::numeric;


-- Select the count of each value of revenues_change
SELECT revenues_change, 
       count(*) AS count
  FROM fortune500
 GROUP BY revenues_change
 -- order by the values of revenues_change
 ORDER BY revenues_change;



-- Select the count of each revenues_change integer value
SELECT revenues_change::integer, count(*)
  FROM fortune500
 GROUP BY revenues_change::integer
 -- order by the values of revenues_change
 ORDER BY revenues_change::integer;


-- Count rows 
SELECT COUNT(*)
  FROM fortune500
 -- Where...
 WHERE revenues_change > 0;


 