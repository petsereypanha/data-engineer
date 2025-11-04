# Store the multi-line cooking instructions
# Step 1: Boil water in a large pot
# Step 2: Add pasta and cook for 10 minutes
# Step 3: Drain and serve with sauce
cooking_instructions = """Step 1: Boil water in a large pot
Step 2: Add pasta and cook for 10 minutes
Step 3: Drain and serve with sauce"""

print(cooking_instructions)

pasta_type = "pasta"

# Update pasta type to be more specific
pasta_type = pasta_type.replace("pasta","fusilli pasta")

ingredient_one = "BASIL"

# Standardize ingredient_one to lowercase
ingredient_one = ingredient_one.lower()

print(pasta_type)
print(ingredient_one)

# Create a list of ingredients
ingredients = ["fusilli", "tomatoes", "basil","garlic", "olive oil","salt"]

# Create a list of ingredient quantities
quantities = [500,400,15,20,30,10]

print(ingredients)
print(quantities)

ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]
quantities = [500, 400, 15, 20, 30, 10]

# Get the second ingredient for your preview
second_ingredient = ingredients[1]

print(second_ingredient)

# Extract the last quantity
last_quantity = quantities[-1]

print(last_quantity)

# Get every other ingredient starting from the first
alternate_ingredient = ingredients[0::2]

print(alternate_ingredient)

# Create the recipe dictionary
recipe = {"olive_oil": 30,
# Add garlic
          "garlic": 15,
# Add tomatoes
          "tomatoes": 400}

print(recipe)

# Add basil to the recipe dictionary
recipe["basil"] = 20

print(recipe)

# Get all ingredient names (dict keys view)
ingredient_names = recipe.keys()

# Get all quantities (dict values view)
quantities = recipe.values()

# Get all key-value pairs (dict items view)
recipe_items = recipe.items()

print("Ingredient names:", ingredient_names)
print("Quantities:", quantities)
print("Recipe items:", recipe_items)

# Create a tuple
cup_conversion = (1, 240)

# Check the type
print(type(cup_conversion))

# Convert the all_ingredients list to a set
unique_ingredients = set(ingredients)

print(unique_ingredients)

print(sorted(unique_ingredients))

pantry_stock = {'tomatoes': 500, 'basil': 80, 'fusilli': 1000, 'garlic': 12}
ingredients_needed = {'fusilli': 1000, 'tomatoes': 800, 'basil': 40, 'garlic': 30, 'olive oil': 30, 'salt': 15}
# Check if you have enough tomatoes for the full party
if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]:
    print("Enough tomatoes for the party!")

# Check if you have enough for a smaller gathering
elif pantry_stock["tomatoes"] >= 800 :
    print("Only enough tomatoes for a smaller gathering.")
# Handle the case where you need to buy more
else:
    print("Need to buy tomatoes before the party.")

basil_grams = 40
required_basil = 40
# Check if you have exactly the right amount of basil
if basil_grams == required_basil:
    print('Perfect! You have exactly the right amount of basil.')
else:
    print('You need to adjust your basil quantity.')

ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Loop through each ingredient in the list
for item in ingredients:
    print(item)

# Iterate over the number of ingredients
for item in range(1,7):
    print("Adding ingredient", item)

quantities = [500, 400, 20, 15, 15, 7]

# Loop through each quantity in the recipe
for qty in quantities:
    # Check if it's a large quantity (400g or more)
    if qty >= 400:
        print('Large quantity')
    # Check if it's a medium quantity (200g or more)
    elif qty >= 200:
        print('Medium quantity')
    # Otherwise it's a small quantity
    else:
        print('Small quantity')

recipe = {
    "fusilli": 500,
    "tomatoes": 400,
    "basil": 20,
    "garlic": 15,
    "olive oil": 15,
    "salt": 7
}

# Loop through the recipe dictionary items
for ingredient, qty in recipe.items():
    # Calculate the scaled quantity by multiplying by 2
    scaled_qty = qty * 2

    print(ingredient, ":", scaled_qty, "g")

total_confirmations = 10
guest_count = 0

# Count confirmations using a while loop
while guest_count < total_confirmations:
    guest_count += 1
    print(guest_count, "guests so far!")

print("We have", guest_count, "guests coming!")

total_ingredients = 7
ingredients_checked = 0

# Set up the loop
while ingredients_checked < total_ingredients:
    # Increment the counter
    ingredients_checked += 1
    # Check if less than 4 ingredients reviewed
    if ingredients_checked < 4:
        print("More than half remaining")
    # Check if 6 or fewer ingredients reviewed
    elif ingredients_checked <= 6:
        print("Nearly finished checking")
    else:
        print("All ingredients verified!")

# Create an empty shopping list
shopping_list = []

# Loop through each ingredient and required quantity
for ingredient, required_qty in recipe.items():
    # Check if we need more than what we have
    if  required_qty > pantry_stock[ingredient]:
        # Add the ingredient to our shopping list
        shopping_list.append(ingredient)

# Display the shopping list
print("Shopping list:", shopping_list)

# Count how many items to buy
items_to_buy = 0

for item in shopping_list:
    items_to_buy += 1

# Display results
print("Number of items to buy:", items_to_buy)
print("Items to buy:", shopping_list)

shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, required_qty in recipe.items():
    print(ingredient)

shopping_list = []
scale_factor = 2

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
    # Calculate the amount needed for the party
    needed_amount = amount * scale_factor

shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
    # Calculate the amount needed for the party
    needed_amount = amount * scale_factor

    # Check if we need to buy this ingredient
    if ingredient not in pantry_stock or needed_amount > pantry_stock[ingredient]:
        shopping_list.append(ingredient)

print("Shopping list for your party:")
print(shopping_list)