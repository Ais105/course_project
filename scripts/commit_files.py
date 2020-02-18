import os
from github import Github
from utils.painter import paint

if __name__ == '__main__':
    print(os.environ['user_name'])
    user = os.environ['user_name']
    password = os.environ['user_password']
    g = Github(user,password)
    user = g.get_user()

    repositories = [repo.name for repo in g.get_user().get_repos()]
    print(repositories)
    repository_name = input("Enter repo name: \n")
    if repository_name not in repositories:
        print("Input repository doesn't exist")

    print("count of commits: ",g.get_user().get_repo(repository_name).get_commits().totalCount)
    commits = g.get_user().get_repo(repository_name).get_commits()
    files_in_commits = {commit.sha: [file.filename for file in commit.files] for commit in commits}
    commits_name = list(files_in_commits.keys())
    last = commits[0]
    commit_list = [file.filename for file in last.files]
    print("last change: ",commit_list)

    paint(commits_name, [files_in_commits[name] for name in commits_name], 10000, 1000)
