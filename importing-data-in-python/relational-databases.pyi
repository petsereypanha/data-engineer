# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Get the table names from the database
table_names = engine.table_names()

# Print the table names
print(table_names)