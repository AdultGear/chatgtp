import requests

# Prompt the user for the necessary information
token = input("Please enter your GitHub token: ")
owner = input("Please enter the repository owner's username: ")
repo = input("Please enter the repository name: ")

headers = {'Authorization': f'token {token}'}

# Base URL for the GitHub API
base_url = 'https://api.github.com'

# Function to create a feature request
def create_feature_request(token, owner, repo, title, body):
    # The 'labels' field can be used to add labels to the issue
    issue = {'title': title, 'body': body, 'labels': ['feature request']}
    response = requests.post(f'{base_url}/repos/{owner}/{repo}/issues', headers=headers, json=issue)
    
    # Check the status code of the response
    if response.status_code != 201:
        print(f"Error creating feature request: {response.status_code}")
        return None

    data = response.json()
    return data

# Create a feature request
title = "Add else statement"
body = "I think we should add an else statement to handle the case where the condition is not met."
feature_request = create_feature_request(token, owner, repo, title, body)
if feature_request is not None:
    print(feature_request)
