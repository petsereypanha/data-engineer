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

# Store the API token in a variable
API_TOKEN = '8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'

headers = {
    'Authorization': 'Bearer ' + API_TOKEN,
    # Add a header to request JSON formatted data
    'Accept': 'application/json'
}
response = requests.get('http://localhost:3000/albums/1/', headers=headers)

# Get the JSON data as a Python object from the response object
album = response.json()

# Print the album title
print(album['Title'])


playlists = [{"Name":"Rock ballads"}, {"Name":"My favorite songs"}, {"Name":"Road Trip"}]

# POST the playlists array to the API using the json argument
requests.post('http://localhost:3000/playlists/', json=playlists)

# Get the list of all created playlists
response = requests.get('http://localhost:3000/playlists')

# Print the response text to inspect the JSON text
print(response.text)

# Import the correct exception class
from requests.exceptions import ConnectionError

url ="http://wronghost:3000/albums"
try:
    r = requests.get(url)
    print(r.status_code)
# Use the imported class to intercept the connection error
except ConnectionError as conn_err:
    print(f'Connection Error! {conn_err}.')

# Import the correct exception class
from requests.exceptions import HTTPError

url ="http://localhost:3000/albums/"
try:
    r = requests.get(url)
	# Enable raising errors for all error status_codes
    r.raise_for_status()
    print(r.status_code)
# Intercept the error
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')

import time

while True:
    params = {'page': page_number, 'per_page': 500}
    response = requests.get('http://localhost:3000/tracks', params=params, headers=headers)
    response.raise_for_status()
    response_data = response.json()

    print(f'Fetching tracks page {page_number}')

    if len(response_data['results']) == 0:
        break

    for track in response_data['results']:
        if track['Length'] > longestTrackLength:
            longestTrackLength = track['Length']
            longestTrackTitle = track['Name']

    page_number = page_number + 1

    # Add your fix here
    time.sleep(3)

print('The longest track in my music library is: ' + longestTrackTitle)
