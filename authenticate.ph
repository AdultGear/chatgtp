# Import the requests library, which allows you to send HTTP requests in Python
import requests

# This is your personal access token from GitHub. Replace 'your_token_here' with your actual token.
# This token is used to authenticate your requests to the GitHub API.
token = 'your_token_here'

# This is a dictionary that will be sent as the headers of your HTTP request.
# The 'Authorization' field is used to pass your token to the GitHub API.
headers = {'Authorization': f'token {token}'}

# This line sends a GET request to the /user endpoint of the GitHub API.
# The headers parameter is set to the headers dictionary, which includes your token.
response = requests.get('https://api.github.com/user', headers=headers)

# The .json() method is called on the response object to parse the JSON response from the GitHub API.
# The result is a dictionary that contains the data returned by the API.
data = response.json()

# This line prints the data returned by the API.
print(data)
