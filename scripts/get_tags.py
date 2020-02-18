import os
from github import Github
from utils.painter import paint

if __name__ == '__main__':
    user = os.environ['user_name']
    password = os.environ['user_password']

    g = Github(user,password)
    user = g.get_user()
    repositories = [repo.name for repo in g.get_user().get_repos()]
    print(repositories)

    repository_name = input("Enter repo name: \n")

    if repository_name not in repositories:
        print("Input repository doesn't exist")

    tags = g.get_user().get_repo(repository_name).get_tags()
    tags_id_list = []
    for tag in tags:
        tags_id_list.append(tag.name)

    paint([repository_name], [tags_id_list], 500, 1000)
