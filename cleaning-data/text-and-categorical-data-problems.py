#import necessary libraries
import pandas as pd
#load airlines data
airlines = pd.read_csv('data/airlines_final.csv')
#load categories data
categories = pd.read_csv('data/categories.csv')

# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique())
print('Safety: ', airlines['safety'].unique())
print('Satisfaction: ', airlines['satisfaction'].unique())

# Find the cleanliness category in airlines not in categories
cat_clean =  set(airlines['cleanliness']) - set(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])