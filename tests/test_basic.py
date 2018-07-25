from .context import app
from aness import __version__ as v
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_version(self):
        self.assertIsNotNone(v.__version__)

    def test_absolute_truth_and_meaning(self):
        self.assertTrue(True)
        self.assertIsNotNone(app)


if __name__ == '__main__':
    unittest.main()
