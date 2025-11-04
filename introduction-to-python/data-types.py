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