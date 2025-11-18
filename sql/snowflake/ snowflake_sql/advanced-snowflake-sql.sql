SELECT
    -- Get the pizza category
    pt.category,
    SUM(p.price * od.quantity) AS total_revenue
FROM order_details AS od
NATURAL JOIN pizzas AS p
-- NATURAL JOIN the pizza_type table
NATURAL JOIN pizza_type AS pt
-- GROUP the records by category
GROUP BY pt.category
-- ORDER by total_revenue and limit the records
ORDER BY total_revenue DESC
LIMIT 1;

SELECT COUNT(o.order_id) AS total_orders,
        AVG(p.price) AS average_price,
        -- Calculate total revenue
        SUM(p.price * od.quantity) AS total_revenue	
FROM orders AS o
LEFT JOIN order_details AS od
ON o.order_id = od.order_id
-- Use an appropriate JOIN with the pizzas table
LEFT JOIN pizzas AS p
ON od.pizza_id = p.pizza_id

SELECT COUNT(o.order_id) AS total_orders,
        AVG(p.price) AS average_price,
        -- Calculate total revenue
        SUM(p.price * od.quantity) AS total_revenue,
        -- Get the name from the pizza_type table
        pt.name AS pizza_name
FROM orders AS o
LEFT JOIN order_details AS od
ON o.order_id = od.order_id
-- Use an appropriate JOIN with the pizzas table
RIGHT JOIN pizzas p
ON od.pizza_id = p.pizza_id
-- NATURAL JOIN the pizza_type table
NATURAL JOIN pizza_type AS pt
GROUP BY pt.name, pt.category
ORDER BY total_revenue desc, total_orders desc;

SELECT pt.name,
    pt.category,
    SUM(od.quantity) AS total_orders
FROM pizza_type pt
JOIN pizzas p
    ON pt.pizza_type_id = p.pizza_type_id
JOIN order_details od
    ON p.pizza_id = od.pizza_id
GROUP BY ALL
HAVING SUM(od.quantity) < (
  -- Calculate AVG of total_quantity
  SELECT AVG(total_quantity)
  FROM (
    -- Calculate total_quantity
    SELECT SUM(od.quantity) AS total_quantity
    FROM pizzas p
    JOIN order_details od 
        ON p.pizza_id = od.pizza_id
    GROUP BY p.pizza_id
    -- Alias as subquery
  ) subquery
)

-- Create a CTE named most_ordered and limit the results 
WITH most_ordered AS (
    SELECT pizza_id, SUM(quantity) AS total_qty 
    FROM order_details GROUP BY pizza_id ORDER BY total_qty DESC
    LIMIT 1
)
-- Create CTE cheapest_pizza where price is equal to min price from pizzas table
, cheapest_pizza AS (
    SELECT pizza_id, price
    FROM pizzas 
    WHERE price = (SELECT MIN(price) FROM pizzas)
    LIMIT 1
)

SELECT pizza_id, 'Most Ordered' AS Description, total_qty AS metric
-- Select from the most_ordered CTE
FROM most_ordered
UNION ALL
SELECT pizza_id, 'Cheapest' AS Description, price AS metric
-- Select from the cheapest_pizza CTE
FROM cheapest_pizza


WITH filtered_orders AS (
  SELECT order_id, order_date 
  FROM orders 
  -- Filter records where order_date is greater than November 1, 2015
  WHERE order_date > '2015-11-01'
)

, filtered_pizza_type AS (
  SELECT name, pizza_type_id 
  FROM pizza_type 
  -- Filter the pizzas which are in the Veggie category
  WHERE category = 'Veggie'
)

SELECT fo.order_id, fo.order_date, fpt.name, od.quantity
-- Get the details from filtered_orders CTE
FROM filtered_orders AS fo
JOIN order_details AS od ON fo.order_id = od.order_id
JOIN pizzas AS p ON od.pizza_id = p.pizza_id
-- JOIN the filtered_pizza_type CTE on pizza_type_id
JOIN filtered_pizza_type AS fpt ON p.pizza_type_id = fpt.pizza_type_id;


SELECT name,
    review_count,
    -- Retrieve the Saturday hours
    hours:Saturday,
    -- Retrieve the Sunday hours
    hours:Sunday
FROM yelp_business_data
-- Filter for Restaurants
WHERE categories LIKE '%Restaurant%'
    AND (hours:Saturday IS NOT NULL AND hours:Sunday IS NOT NULL)
    AND city = 'Philadelphia'
    AND stars = 5
ORDER BY review_count DESC


SELECT business_id, name
FROM yelp_business_data
WHERE categories ILIKE '%Restaurant%'
    -- Filter where DogsAllowed is '%True%'
    AND attributes:DogsAllowed ILIKE '%True%'
    -- Filter where BusinessAcceptsCreditCards is '%True%'
    AND attributes:BusinessAcceptsCreditCards ILIKE '%True%'
    AND city ILIKE '%Philadelphia%'
    AND stars = 5;