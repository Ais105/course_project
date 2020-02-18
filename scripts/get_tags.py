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

    repository_name = input("Enter repo name: \n")

    if repository_name not in repositories:
        print("Input repository doesn't exist")

    tag_names = client.get_tags_name(repository_name)

    paint([repository_name], [tag_names], 500, 1000)
