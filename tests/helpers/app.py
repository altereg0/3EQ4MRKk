import copy
import json
import aumbry

from aness.app import AlterService
from aness.config import AppConfig
from falcon import testing
from aness.helpers import generate_path


class AppTestCase(testing.TestCase):
    def setUp(self):
        super(AppTestCase, self).setUp()
        # Assume the hypothetical `myapp` package has a
        # function called `create()` to initialize and
        # return a `backend.API` instance.
        # self.app = myapp.create()
        # self.mysqld = self.Mysqld()

        cfg = aumbry.load(
            aumbry.FILE,
            AppConfig,
            {
                'CONFIG_FILE_PATH': './etc/config.yml'
            }
        )
        self.app = AlterService(cfg)
        self.api_version = cfg.api_version
        self.prefix = 'api'

    def tearDown(self):
        # Shutdown database connection
        pass

    def _path(self, uri_template):
        return generate_path(self.prefix, self.api_version, uri_template)

    @classmethod
    def setUpClass(cls):
        # cls.Mysqld = testing.mysqld.MysqldFactory(cache_initialized_db=True)
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.Mysqld.clear_cache()
        pass

    def get_headers(self, headers):
        all_headers = {}

        if headers:
            all_headers.update(copy.deepcopy(headers))

        return all_headers

    def get(self, path, params=None, headers=None):
        return self.simulate_get(
            self._path(path),
            params=params,
            headers=self.get_headers(headers)
        )

    def post(self, path, body=None, params=None, headers=None):
        return self.simulate_post(
            self._path(path),
            body=body,
            params=params,
            headers=self.get_headers(headers)
        )

    def put(self, path, body=None, params=None, headers=None):
        return self.simulate_put(
            self._path(path),
            body=body,
            params=params,
            headers=self.get_headers(headers)
        )

    def delete(self, path, params=None, headers=None):
        return self.simulate_delete(
            self._path(path),
            params=params,
            headers=self.get_headers(headers)
        )

    def post_json(self, path, body, params=None, headers=None):
        return self.post(
            path,
            json.dumps(body),
            params,
            headers)
