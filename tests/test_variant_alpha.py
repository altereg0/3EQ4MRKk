# -----------------------------------------------------------------
# unittest
# -----------------------------------------------------------------
from tests.helpers import app


# from unittest import skip


class TestUsersResource(app.AppTestCase):
    def test_can_create(self):
        post_req = self.post_json(
            'users',
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
        """
        hmmm... should be more verbose output from 'green', but nope....
        """
        post_req = self.post_json(
            'users',
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

        get_req = self.get('users')
        self.assertEqual(get_req.status_code, 200)

        users_list = get_req.json['data']
        self.assertEqual(len(users_list), 1)

        post_req = self.post_json(
            'users',
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

        get_req = self.get('users')
        self.assertEqual(get_req.status_code, 200)

        users_list = get_req.json['data']
        self.assertEqual(len(users_list), 2)

    def test_api(self):
        get_req = self.get('')
        self.assertEqual(get_req.status_code, 200)

        media = get_req.json
        self.assertEqual(media['data']['id'], get_req.headers['REQUEST-ID'])


class TestAdvertResource(app.AppTestCase):
    def test_can_create(self):
        """Test ADVERT resource"""
        post_req = self.post_json(
            'users',
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

        post_req = self.post_json(
            'adverts',
            {
                "data": {
                    "relationships": {
                        "author": {
                            "data": {
                                "type": "user",
                                "id": "1"
                            }
                        }
                    },
                    "type": "advert",
                    "attributes": {
                        "title": "Aves",
                        "description": "Anything cools"
                    }
                }
            }
        )
        self.assertEqual(post_req.status_code, 201)
        self.assertEqual(post_req.json.get('id'), 1)

    def test_can_list(self):
        """
        hmmm... should be more verbose output from 'green', but nope....
        """
        post_req = self.post_json(
            'users',
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

        post_req = self.post_json(
            'adverts',
            {
                "data": {
                    "relationships": {
                        "author": {
                            "data": {
                                "type": "user",
                                "id": "1"
                            }
                        }
                    },
                    "type": "advert",
                    "attributes": {
                        "title": "Aves",
                        "description": "Anything cools"
                    }
                }
            }
        )
        self.assertEqual(post_req.status_code, 201)
        self.assertEqual(post_req.json.get('id'), 1)

        post_req = self.post_json(
            'adverts',
            {
                "data": {
                    "relationships": {
                        "author": {
                            "data": {
                                "type": "user",
                                "id": "1"
                            }
                        }
                    },
                    "type": "advert",
                    "attributes": {
                        "title": "Aves",
                        "description": "Anything cools"
                    }
                }
            }
        )
        self.assertEqual(post_req.status_code, 201)
        self.assertEqual(post_req.json.get('id'), 2)

        get_req = self.get('adverts')
        self.assertEqual(get_req.status_code, 200)

        adverts_list = get_req.json['data']
        self.assertEqual(len(adverts_list), 2)
