from .context import app

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        self.assertTrue(True)
        self.assertIsNotNone(app)


if __name__ == '__main__':
    unittest.main()
