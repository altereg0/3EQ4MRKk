from tests.helpers import app
from aness.helpers import FuckingFactory


class AdvancedTestSuite(app.AppTestCase):
    """Advanced test cases."""

    def setUp(self):
        super(AdvancedTestSuite, self).setUp()
        self.num_accounts = 50
        self.num_adverts = 8

        FuckingFactory.generate_mock_data(num_users=self.num_accounts, num_max_adverts_per_user=self.num_adverts)

    def test_mock_data(self):
        get_req = self.get('users')
        self.assertEqual(get_req.status_code, 200)

        users_list = get_req.json['data']
        self.assertEqual(len(users_list), self.num_accounts)

        get_req = self.get('adverts')
        self.assertEqual(get_req.status_code, 200)

        users_list = get_req.json['data']
        self.assertEqual(len(users_list), self.num_adverts)
