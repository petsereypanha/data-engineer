# Import packages
from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt

# Assign url of file: url
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

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
url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xls
xls = pd.ExcelFile(url)


# Print the sheetnames to the shell
print(xls.sheet_names)

# Print the head of the first sheet (using its name, NOT its index)
print(xls.parse(xls.sheet_names[0]).head())

# Import packages
from urllib.request import urlopen, Request
import ssl

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request: request
request = Request(url)

# Create an unverified SSL context
context = ssl._create_unverified_context()

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()

# Import the requests package
import requests

# Assign URL to variable: url
url = 'http://www.datacamp.com/teach/documentation'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response text: text
text = r.text

# Print the HTML of the webpage
print(text)
