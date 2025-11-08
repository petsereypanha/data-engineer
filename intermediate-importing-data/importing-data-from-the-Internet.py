# Import packages
from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt

# Assign url of file: url
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
url = 'data/winequality-red.csv'
# Read file into a DataFrame and print its head
df = pd.read_csv(url, sep=';')
print(df.head())

# Plot first column of df
df.iloc[:, 0].hist()
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()


# Import package
import pandas as pd

# Assign url of file: url
# url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'
url = 'data/latitude.xls'

# Read in all sheets of Excel file: xls
xls = pd.ExcelFile(url)


# Print the sheetnames to the shell
print(xls.sheet_names)

# Print the head of the first sheet (using its name, NOT its index)
print(xls.parse(xls.sheet_names[0]).head())
