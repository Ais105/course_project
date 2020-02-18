import os
from github_client.client import GitHubClient
from utils.painter import paint

if __name__ == '__main__':
    print(os.environ['user_name'])
    user = os.environ['user_name']
    password = os.environ['user_password']

    client = GitHubClient(user, password)
    client.connect()
    repositories = client.get_repositories()
    print(repositories)
    repository_name = input("Enter repo name: \n")
    if repository_name not in repositories:
        print("Input repository doesn't exist")

    print("count of commits: ", client.get_commits_count(repository_name))
    commits = client.get_commits(repository_name)
    files_in_commits = client.get_files_in_commits(commits)
    commits_name = client.get_commits_name(files_in_commits)

    paint(commits_name, [files_in_commits[name] for name in commits_name], 10000, 1000)
