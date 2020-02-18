import pytest, unittest, os
class Test_log:
    def test_logging(self):
        log = os.environ['user_name']
        assert log != KeyError
    def test_pass(self):
        pas = os.environ['user_password']
        assert pas != KeyError




