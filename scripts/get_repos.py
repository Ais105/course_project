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
    user = client.get_user()
    paint([user.login], [repositories], 500, 10000)
