import unittest
import os


class TestEnvironment(unittest.TestCase):

    def setUp(self) -> None:
        if os.environ.get("user_name1"):
            del os.environ['user_name1']
        if os.environ.get("password1"):
            del os.environ['password1']

    def test_environments_absent(self):
        with self.assertRaises(KeyError):
            user_name = os.environ['user_name1']
        with self.assertRaises(KeyError):
            password = os.environ['password1']

    def test_environments_exist(self):
        os.environ["user_name1"] = "cool_user"
        os.environ["user_password1"] = "secure_password"

        self.assertEqual(os.environ['user_name1'], "cool_user")
        self.assertEqual(os.environ['user_password1'], "secure_password")


if __name__ == '__main__':
    unittest.main()
