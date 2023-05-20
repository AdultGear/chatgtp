import requests

# Your personal access token
token = 'your_token_here'
headers = {'Authorization': f'token {token}'}

# Base URL for the GitHub API
base_url = 'https://api.github.com'

# Function to get a repository
def get_repo(owner, repo):
    response = requests.get(f'{base_url}/repos/{owner}/{repo}', headers=headers)
    data = response.json()
    return data

# Function to list issues on a repository
def list_issues(owner, repo):
    response = requests.get(f'{base_url}/repos/{owner}/{repo}/issues', headers=headers)
    data = response.json()
    return data

# Function to create an issue
def create_issue(owner, repo, title, body):
    issue = {'title': title, 'body': body}
    response = requests.post(f'{base_url}/repos/{owner}/{repo}/issues', headers=headers, json=issue)
    data = response.json()
    return data

# Replace 'owner' and 'repo' with the owner and name of the repository you're interested in
owner = 'owner'
repo = 'repo'

# Get a repository
repo_data = get_repo(owner, repo)
print(repo_data)

# List issues on a repository
issues = list_issues(owner, repo)
print(issues)

# Create an issue
new_issue = create_issue(owner, repo, 'New issue', 'This is a new issue.')
print(new_issue)
