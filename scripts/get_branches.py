import os
from github_client.client import GitHubClient
from utils.painter import paint

if __name__ == '__main__':
    os.environ["user_name"] = "Ais105"
    os.environ["user_password"] = "m123j54der"
    user = os.environ['user_name']
    password = os.environ['user_password']
    client = GitHubClient(user, password)
    client.connect()
    repositories = client.get_repositories()
    print(repositories)

    # get all branches
    repository_name = input("Enter repo name: \n")
    if repository_name not in repositories:
        print("Input repository doesn't exist")
    branches_name = client.get_branches_name(repository_name)

    paint([repository_name], [branches_name], 400, 500)
