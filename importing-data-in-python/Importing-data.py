# # Import pickle package
# import pickle
#
# # Open pickle file and load data: d
# with open('data.pkl', 'rb') as file:
#     d = pickle.load(file)
#
# # Print d
# print(d)
#
# # Print datatype of d
# print(type(d))

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'data/battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the first sheet and rename the column: df2
df2 = xls.parse(0, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())
