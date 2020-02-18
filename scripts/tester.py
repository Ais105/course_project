"""
    [X] repos
    [X] branches
    [X] files for commit
    [X] tags
    [X] submodules
    [ ] bags for changed files

"""
import git
import os
import shutil

from github_client.client import GitHubClient

from utils.painter import paint

if __name__ == '__main__':
    os.environ["user_name"] = "Ais105"
    os.environ["user_password"] = "m123j54der"
    user = os.environ['user_name']
    password = os.environ['user_password']

    client = GitHubClient(user, password)
    client.connect()
    user = client.get_user()

    # get repositories
    repositories = client.get_repositories()
    paint([user.login], [repositories], 500, 10000)

    # get all branches name
    repository_name = input("Enter repo name: \n")
    print("Get all branches in repo %s:" % repository_name)
    if repository_name not in repositories:
        print("Input repository doesn't exist")
    branches_name = client.get_branches_name(repository_name)
    paint([repository_name], [branches_name], 400, 500)

    # get all tags name
    repository_name = input("Get repo for tags: \n")
    print("Get all tags in repo %s:" % repository_name)
    tag_names = client.get_tags_name(repository_name)
    paint([repository_name], [tag_names], 500, 130000)

    # commits_files
    print("Get all commits in repository %s:" % repository_name)
    repository_name = input("Get repo for commits: \n")
    print("count of commits: ", client.get_commits_count(repository_name))
    commits = client.get_commits(repository_name)
    files_in_commits = client.get_files_in_commits(commits)
    commits_name = client.get_commits_name(files_in_commits)
    last = commits[0]
    commit_list = [file.filename for file in last.files]
    print("last change: ", commit_list)
    paint(commits_name, [files_in_commits[name] for name in commits_name], 10000, 20000)

    # get submodules
    repository_name = input("Get repo for subs: \n")
    repository_url = client.get_url_repository(repository_name)
    DIR_NAME = "your_clone_rep"
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
