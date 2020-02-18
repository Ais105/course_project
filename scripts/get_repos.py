import os
from github import Github
from utils.painter import paint

if __name__ == '__main__':
    user = os.environ['user_name']
    password = os.environ['user_password']
    g = Github(user,password)
    user = g.get_user()

    repositories = [repo.name for repo in g.get_user().get_repos()]
    paint([user.login], [repositories], 500, 10000)
