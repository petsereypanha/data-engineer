#import the requests library
import requests

# Create the authentication tuple with the correct values for basic authentication
authentication = ('user1', 'password1')

# Use the correct function argument to pass the authentication tuple to the API
response = requests.get('http://localhost:3000/albums', auth=authentication)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')

# Create a dictionary containing the API key using the correct key-value combination
params = {'access_token': '8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
# Add the dictionary to the requests.get() call using the correct function argument
response = requests.get('http://localhost:3000/albums', params=params)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')

# Create a headers dictionary containing and set the API key using the correct key and value
headers = {'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
# Add the headers dictionary to the requests.get() call using the correct function argument
response = requests.get('http://localhost:3000/albums', headers=headers)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')

