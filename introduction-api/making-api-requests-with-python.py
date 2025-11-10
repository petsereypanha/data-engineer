from urllib.request import urlopen

with urlopen('http://localhost:3000/lyrics/') as response:
    # Use the correct function to read the response data from the response object
    data = response.read()
    encoding = response.headers.get_content_charset()

    # Decode the response data so you can print it as a string later
    string = data.decode(encoding)

    print(string)

# Import the requests package
import requests

# Pass the API URL to the get function
response = requests.get('http://localhost:3000/lyrics/')

# Print out the text attribute of the response object
print(response.text)

# Construct the URL string and pass it to the requests.get() function
response = requests.get('http://localhost:3000/lyrics/random')

print(response.text)

# Create a dictionary variable with query params
query_params = { 'artist': 'Deep Purple'}

# Pass the dictionary to the get() function
response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

print(response.text)

# Add the `include_track` parameter
query_params = { 'artist': 'Deep Purple', 'include_track': True}

response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

# Print the response URL
print(response.url)

# Print the lyric
print(response.text)

# Get a list of all playlists from the API
response = requests.get('http://localhost:3000/playlists')
print(response.text)

# Create a dictionary with the playlist info
playlist_data = {"Name": 'Rock Ballads'}

# Perform a POST request to the playlists API with your dictionary as data parameter
response = requests.post('http://localhost:3000/playlists', data=playlist_data)
print(response.text)

# Perform a GET request to get info on playlist with PlaylistId 2
response = requests.get('http://localhost:3000/playlists/2')

print(response.text)

# Perform a DELETE request to the playlist API using the path to playlist with PlaylistId 2
requests.delete('http://localhost:3000/playlists/2')

# Get the list of all existing playlists again
response = requests.get('http://localhost:3000/playlists')
print(response.text)

# Make a request to the movies endpoint of the API
response = requests.get('http://localhost:3000/____')

if (response.status_code == 200):
    print('The server responded succesfully!')

# Check the response status code
elif (response.status_code == 404):
    print('Oops, that API could not be found!')

response = requests.get('http://localhost:3000/lyrics')

# Print the response content-type header
print(response.headers['Content-Type'])

# Print the response accept header
print(response.headers['Accept'])

# Set the content type to application/json
headers = {'accept': 'application/json'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Print the response's text
print(response.text)

#  Add a header to use in the request
headers = {'accept': 'application/xml'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
if (response.status_code == 406):
    print('The server can not respond in XML')

    # Print the accepted content types
    print('These are the content types the server accepts: ' + response.headers['Accept'])
else:
    print(response.text)