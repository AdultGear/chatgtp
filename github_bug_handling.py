import requests

# Prompt the user for the necessary information
token = input("Please enter your GitHub token: ")
owner = input("Please enter the repository owner's username: ")
repo = input("Please enter the repository name: ")

headers = {'Authorization': f'token {token}'}

# Base URL for the GitHub API
base_url = 'https://api.github.com'

# Function to list issues labeled as "bug"
def list_bugs(token, owner, repo):
    # The 'labels' parameter can be used to filter issues by label
    response = requests.get(f'{base_url}/repos/{owner}/{repo}/issues', headers=headers, params={'labels': 'bug'})
    
    # Check the status code of the response
    if response.status_code != 200:
        print(f"Error getting issues: {response.status_code}")
        return None

    data = response.json()
    return data

# Function to close an issue
def close_issue(token, owner, repo, issue_number):
    # The 'state' field of an issue can be 'open' or 'closed'
    issue = {'state': 'closed'}
    response = requests.patch(f'{base_url}/repos/{owner}/{repo}/issues/{issue_number}', headers=headers, json=issue)
    
    # Check the status code of the response
    if response.status_code != 200:
        print(f"Error closing issue: {response.status_code}")
        return None

    data = response.json()
    return data

# List issues labeled as "bug"
bugs = list_bugs(token, owner, repo)
if bugs is not None:
    print(bugs)

# Close the first bug
if bugs:
    closed_bug = close_issue(token, owner, repo, bugs[0]['number'])
    if closed_bug is not None:
        print(closed_bug)
