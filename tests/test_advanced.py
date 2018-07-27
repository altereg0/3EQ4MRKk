from tests.helpers import app
from aness.helpers import generate_mock_data
class AdvancedTestSuite(app.AppTestCase):
    """Advanced test cases."""
    
    def setUp(self):
        super(AdvancedTestSuite, self).setUp()
        self.num_accounts = 1000
        generate_mock_data(num=self.num_accounts)


    def test_thoughts(self):
        get_req = self.get('users')
        self.assertEqual(get_req.status_code, 200)

        users_list = get_req.json['data']
        self.assertEqual(len(users_list), self.num_accounts)