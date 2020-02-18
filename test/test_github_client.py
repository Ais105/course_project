import os
import unittest
from github_client.client import GitHubClient
from github.GithubException import BadCredentialsException, UnknownObjectException


class TestGitHubClient(unittest.TestCase):

    def test_invalid_credentials(self):
        os.environ["user_name1"] = "invalid_username"
        os.environ["user_password1"] = "invalid_password"

        username = os.environ['user_name1']
        password = os.environ['user_password1']

        client = GitHubClient(username, password)
        with self.assertRaises(BadCredentialsException):
            client.connect()

    def test_repository_name_absent_in_query_get_commits_count(self):
        username = os.environ['user_name']
        password = os.environ['user_password']

        client = GitHubClient(username, password)
        client.connect()
        with self.assertRaises(UnknownObjectException):
            client.get_commits_count("invalid_repository_name")

    def test_repository_name_absent_in_query_get_commits(self):
        username = os.environ['user_name']
        password = os.environ['user_password']

        client = GitHubClient(username, password)
        client.connect()
        with self.assertRaises(UnknownObjectException):
            client.get_commits_count("invalid_repository_name")

    def test_repository_name_absent_in_query_get_branches_name(self):
        username = os.environ['user_name']
        password = os.environ['user_password']

        client = GitHubClient(username, password)
        client.connect()
        with self.assertRaises(UnknownObjectException):
            client.get_commits_count("invalid_repository_name")

    def test_repository_name_absent_in_query_get_tags_name(self):
        username = os.environ['user_name']
        password = os.environ['user_password']

        client = GitHubClient(username, password)
        client.connect()
        with self.assertRaises(UnknownObjectException):
            client.get_commits_count("invalid_repository_name")

    def test_repository_name_absent_in_query_get_url_repository(self):
        username = os.environ['user_name']
        password = os.environ['user_password']

        client = GitHubClient(username, password)
        client.connect()
        with self.assertRaises(UnknownObjectException):
            client.get_commits_count("invalid_repository_name")


if __name__ == '__main__':
    unittest.main()
