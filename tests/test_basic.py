from tests.helpers import app
from aness import __version__ as v


class BasicTestSuite(app.AppTestCase):
    """Basic test cases."""

    def test_version(self):
        self.assertIsNotNone(v.__version__)

    def test_absolute_truth_and_meaning(self):
        self.assertTrue(True)
        self.assertTrue(42)

        self.assertIsNotNone(app)
