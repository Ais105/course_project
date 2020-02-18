"""
    [X] repos
    [X] branches
    [X] files for commit
    [X] tags
    [X] submodules
    [ ] bags for changed files

"""
import shutil, git, os
from github import Github
from utils.painter import paint

if __name__ == '__main__':
    user = os.environ['user_name']
    password = os.environ['user_password']
    g = Github(user,password)
    user = g.get_user()

    #get repos
    repositories = [repo.name for repo in g.get_user().get_repos()]
    paint([user.login], [repositories], 500, 10000)

    #get all branches
    repository_name = input("Enter repo name: \n")
    print("Get all branches in repo %s:" % repository_name)
    if repository_name not in repositories:
        print("Input repository doesn't exist")
    branches = [branch.name for branch in g.get_user().get_repo(repository_name).get_branches()]
    paint([repository_name], [branches], 400, 500)

    r_name = input("Get repo for tags: \n")
    print("Get all tags in repo %s:" % r_name)
    tags = g.get_user().get_repo(repository_name).get_tags()
    tags_id_list = []
    for tag in tags:
        tags_id_list.append(tag.name)
    paint([r_name], [tags_id_list], 500, 130000)

    # commits_files
    print("Get all commits in repository %s:" % repository_name)
    rep_name = input("Get repo for commits: \n")
    print("count of commits: ",g.get_user().get_repo(rep_name).get_commits().totalCount)
    commits = g.get_user().get_repo(rep_name).get_commits()
    files_in_commits = {commit.sha: [file.filename for file in commit.files] for commit in commits}
    commits_name = list(files_in_commits.keys())
    last = commits[0]
    commit_list = [file.filename for file in last.files]
    print("last change: ",commit_list)

    paint(commits_name, [files_in_commits[name] for name in commits_name], 10000, 20000)

    repo_name = input("Get repo for subs: \n")
    l = g.get_user().get_repo(repo_name).html_url
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

    paint([repo_name], [arr], 500, 130000)
