import os
import time
import git

repos = [
    {'name': 'httpie/httpie', 'path': 'httpie'},
    {'name': 'pallets/flask', 'path': 'flask'}
]

def get_latest_commit_message(repo_path):
    repo = git.Repo(repo_path)
    return repo.head.commit.message

def check_for_new_commits(repo):
    repo_path = repo['path']
    repo_name = repo['name']

    # Move to repo directory
    os.chdir(repo_path)

    # Fetch the latest changes from the remote
    os.system('git fetch')

    # Compare the local HEAD to the remote HEAD
    local_commit = os.popen('git rev-parse HEAD').read().strip()
    remote_commit = os.popen('git rev-parse @{u}').read().strip()

    if local_commit != remote_commit:
        print(f"New commit detected in {repo_name}!")
        print(f"Latest commit message: {get_latest_commit_message(repo_path)}")
        os.system('git pull')
    else:
        print(f"Repo {repo_name} is up-to-date!")

    # Move back to the previous directory
    os.chdir('..')

while True:
    for repo in repos:
        check_for_new_commits(repo)
    time.sleep(15)  # Check every 15 seconds
