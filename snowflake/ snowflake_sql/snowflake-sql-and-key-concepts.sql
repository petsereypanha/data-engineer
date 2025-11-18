-- Select pizza_type_id, pizza_size, and price from pizzas table
SELECT pizza_type_id,
	pizza_size,
    price
FROM pizzas;

-- Count all pizza entries
SELECT COUNT(*) AS count_all_pizzas
FROM pizza_type;

-- Count all pizza entries
SELECT COUNT(*) AS count_all_pizzas
FROM pizza_type
-- Apply filter on category for Classic pizza types
WHERE category = 'Classic';

-- Get information about the orders table
DESC TABLE orders;

-- Convert order_id to VARCHAR aliasing to order_id_string
SELECT CAST(order_id AS VARCHAR) AS order_id_string
FROM orders;

SELECT price, 
-- Convert price to NUMBER data type
CAST(price AS NUMBER) AS price_dollars
FROM pizzas

-- Capitalize each word in pizza_type_id
SELECT INITCAP(pizza_type_id) AS capitalized_pizza_id 
FROM pizza_type;

-- Combine the name and category columns
SELECT CONCAT(name, ' - ', category) AS name_and_category
FROM pizza_type;

-- Select the current date, current time
SELECT CURRENT_DATE, CURRENT_TIME;

-- Count the number of orders per day
SELECT COUNT(*) AS orders_per_day, 
-- Extract the day of the week and alias to order_day
	EXTRACT(DAYOFWEEK FROM order_date) AS order_day
FROM orders
GROUP BY order_day
ORDER BY orders_per_day DESC

SELECT EXTRACT(MONTH FROM order_date) AS order_month, 
    p.pizza_size, 
    -- Calculate revenue
    SUM(p.price * od.quantity) AS revenue
FROM orders o
INNER JOIN order_details od USING(order_id)
INNER JOIN pizzas p USING(pizza_id)
-- Using Snowflake's GROUP BY ALL
GROUP BY ALL
-- Sort by revenue in descending order
ORDER BY revenue DESC

