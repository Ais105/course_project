import os
from github_client.client import GitHubClient
from utils.painter import paint

if __name__ == '__main__':
    user = os.environ['user_name']
    password = os.environ['user_password']
    client = GitHubClient(user, password)
    client.connect()
    repositories = client.get_repositories()
    user = client.get_user()
    paint([user.login], [repositories], 500, 10000)
