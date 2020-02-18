import shutil, git, os
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

    l = g.get_user().get_repo(repository_name).html_url
    DIR_NAME = "your_clone_rep"
    REMOTE_URL = (l + ".git")

    if os.path.isdir(DIR_NAME):
        shutil.rmtree(DIR_NAME)
    os.mkdir(DIR_NAME)
    repo = git.Repo.init(DIR_NAME)
    origin = repo.create_remote('origin', REMOTE_URL)
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)
    sm = repo.submodules
    arr = [submodule.name for submodule in sm]

    paint([repository_name], [arr], 500, 130000)
