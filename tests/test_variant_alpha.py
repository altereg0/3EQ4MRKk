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
                    "type": "user",
                    "attributes": {
                        "uid": "5772ccd2e6b14dd3",
                        "social": "YELLOW",
                        "name": "Дайна Аброськина"
                    },
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
                    "type": "user",
                    "attributes": {
                        "uid": "90792532401de273",
                        "social": "PURPLE",
                        "name": "Екатерина Трошина"
                    },
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
                    "type": "user",
                    "attributes": {
                        "uid": "5868ca829b560a1d",
                        "social": "BLUE",
                        "name": "Инна Авдюшина"
                    },
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
                    "type": "user",
                    "attributes": {
                        "uid": "930605b7b42af0a4",
                        "social": "PINK",
                        "name": "Ася Токарева"
                    },
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
                    "type": "user",
                    "attributes": {
                        "uid": "fdb07ea6bf687872",
                        "social": "PINK",
                        "name": "Артур Горбунов"
                    },
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
                        "description": "Институциализация формирует диссон\
                        ансный постиндустриализм, о чем будет подробнее ска\
                        зано ниже. Полифонический роман приводит современн\
                        ый контрапункт. М.М.Бахтин понимал тот факт, что д\
                        рама диссонирует феномен толпы, подчеркивает прези\
                        дент. Понятие тоталитаризма ограничивает антрополо\
                        гический пастиш."
                    }
                }
            }
        )
        self.assertEqual(post_req.status_code, 201)
        self.assertEqual(post_req.json.get('id'), 1)