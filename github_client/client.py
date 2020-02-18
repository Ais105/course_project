from github import Github


class GitHubClient:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password
        self._github_api = None
        self._github_user = None
        self._github_repositories = None

    def get_user(self):
        return self._github_user

    def get_repositories(self):
        return self._github_repositories

    def connect(self):
        self._github_api = Github(self._username, self._password)
        self._github_user = self._github_api.get_user()
        self._github_repositories = [repository.name for repository in self._github_user.get_repos()]

    def get_commits_count(self, repository_name):
        return self._github_user.get_repo(repository_name).get_commits().totalCount

    def get_commits(self, repository_name):
        return self._github_user.get_repo(repository_name).get_commits()

    def get_branches_name(self, repository_name):
        return [branch.name for branch in self._github_user.get_repo(repository_name).get_branches()]

    def get_tags_name(self, repository_name):
        return [tag.name for tag in self._github_user.get_repo(repository_name).get_tags()]

    def get_url_repository(self, repository_name):
        return self._github_user.get_repo(repository_name).html_url

    @staticmethod
    def get_files_in_commits(commits):
        return {commit.sha: [file.filename for file in commit.files] for commit in commits}

    @staticmethod
    def get_commits_name(file_in_commits: dict):
        return list(file_in_commits.keys())
