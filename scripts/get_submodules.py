import git
import os
import shutil

from github_client.client import GitHubClient
from utils.painter import paint

DIR_NAME = "your_clone_rep"

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

    repository_url = client.get_url_repository(repository_name)
    REMOTE_URL = (repository_url + ".git")
    os.mkdir(DIR_NAME)
    repo = git.Repo.init(DIR_NAME)
    origin = repo.create_remote('origin', REMOTE_URL)
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)
    sm = repo.submodules
    arr = [submodule.name for submodule in sm]
    if os.path.isdir(DIR_NAME):
        shutil.rmtree(DIR_NAME)

    paint([repository_name], [arr], 500, 130000)
