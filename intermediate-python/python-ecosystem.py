from pyarrow import large_list

recent_orders = [15.99, 28.50, 42.75, 18.99, 55.00, 31.25, 22.99, 67.50]

# Find the smallest order amount
smallest_order = min(recent_orders)

# Find the largest order amount
largest_order =   max(recent_orders)

# Calculate total revenue from all orders
total_revenue =  sum(recent_orders)

print("Smallest order:", smallest_order)
print("Largest order:", largest_order)
print("Total revenue:", total_revenue)

delivery_times = [19, 25, 35, 40, 28, 32, 29, 31]

# Find the average delivery time
average_time =  sum(delivery_times) / len(delivery_times)

# Round the average delivery time to two decimal places
average_rounded = round(average_time, 2)

print("Average delivery time:", average_rounded)

restaurants = ["Sushi Central", "Burger Hub", "Taco Town", "Pizza Palace"]
cooking_times = [30, 25, 35, 40, 28, 32, 29, 31, 12, 55]

# Sort restaurant names alphabetically
restaurants_sorted =sorted(restaurants)

# Sort cooking times from fastest to slowest
cooking_times_sorted = sorted(cooking_times)

print("Restaurants (A–Z):", restaurants_sorted)
print("Cooking times (ascending):", cooking_times_sorted)

# Import the os module
import os

# Get the current working directory
print("Current working directory:", os.getcwd())

# Check the environment variables
print("Environment variables:", os.environ)

# Import the string module
import string

# Print all ASCII lowercase characters
print(string.ascii_lowercase)

# Print all punctuation
print(string.punctuation)