import requests

def get_github_repo_details(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)

    if response.status_code == 200:
        repo_data = response.json()
        is_forked = repo_data['fork']
        project_details = {
            'name': repo_data['name'],
            'description': repo_data['description'],
            'forked': is_forked,
            'forked_from': repo_data['parent']['full_name'] if is_forked else None,
            'url': repo_data['html_url'],
            # Add more fields as needed
        }
        return project_details
    else:
        return None

# Example usage:
repo_owner = "NagiPragalathan"
repo_name = "food-donar-management-system"

repo_details = get_github_repo_details(repo_owner, repo_name)
if repo_details:
    print("Repository Details:")
    print(f"Name: {repo_details['name']}")
    print(f"Description: {repo_details['description']}")
    print(f"Forked: {'Yes' if repo_details['forked'] else 'No'}")
    if repo_details['forked']:
        print(f"Forked From: {repo_details['forked_from']}")
    print(f"URL: {repo_details['url']}")
else:
    print("Failed to fetch repository details.")
