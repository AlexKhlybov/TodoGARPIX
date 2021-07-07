import unittest2 as unittest

from todo import create_app


class BaseTestCase(unittest.TestCase):
    """A base test case"""

    def setUp(self):
        app = create_app("testing")
        app.app_context().push()
        self.app = app.test_client()
