from tests.helpers import app


class TestScoresResource(app.AppTestCase):
    def test_can_create(self):
        req = self.post_json(
            '/scores',
            {
                'username': 'test',
                'company': 'test',
                'score': 100
            }
        )
        self.assertEqual(req.status_code, 201)
        self.assertEqual(req.json.get('id'), 1)

    def test_can_list(self):
        post_req = self.post_json(
            '/scores',
            {
                'username': 'my_user',
                'company': 'test',
                'score': 50
            }
        )
        self.assertEqual(post_req.status_code, 201)

        get_req = self.get('/scores')
        self.assertEqual(get_req.status_code, 200)

        score_list = get_req.json.get('scores')
        self.assertEqual(len(score_list), 1)

    def test_api(self):
        get_req = self.get('/api')
        self.assertEqual(get_req.status_code, 200)

        body = get_req.text
        self.assertEqual(body, 'Server works!')
