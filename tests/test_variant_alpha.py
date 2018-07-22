# -----------------------------------------------------------------
# unittest
# -----------------------------------------------------------------
from tests.helpers import app
# from unittest import skip


class TestUsersResource(app.AppTestCase):
    def test_can_create(self):
        post_req = self.post_json(
            '/api/users',
            {
                "data": {
                    "attributes": {
                        "name": "John Doe",
                        "provider": "any",
                        "uid": "cbi2345"
                    },
                    "type": "user"
                }
            }
        )
        self.assertEqual(post_req.status_code, 201)
        self.assertEqual(post_req.json.get('id'), 1)

    def test_can_list(self):
        post_req = self.post_json(
            '/api/users',
            {
                "data": {
                    "attributes": {
                        "name": "John Doe",
                        "provider": "any",
                        "uid": "cbi2345"
                    },
                    "type": "user"
                }
            }
        )
        self.assertEqual(post_req.status_code, 201)

        get_req = self.get('/api/users')
        self.assertEqual(get_req.status_code, 200)

        users_list = get_req.json['data']
        self.assertEqual(len(users_list), 1)

        post_req = self.post_json(
            '/api/users',
            {
                "data": {
                    "attributes": {
                        "name": "Mary Jane",
                        "provider": "any",
                        "uid": "cb54321"
                    },
                    "type": "user"
                }
            }
        )
        self.assertEqual(post_req.status_code, 201)

        get_req = self.get('/api/users')
        self.assertEqual(get_req.status_code, 200)

        users_list = get_req.json['data']
        self.assertEqual(len(users_list), 2)

    def test_api(self):
        get_req = self.get('/api')
        self.assertEqual(get_req.status_code, 200)

        media = get_req.json
        self.assertEqual(media['foo'], 'bar')
