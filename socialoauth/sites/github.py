# -*- coding: utf-8 -*-

from socialoauth.sites.base import OAuth2


class Github(OAuth2):
    ID = '6bsxhekg'
    AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'

    GITHUB_API_URL_PREFIX = 'https://api.github.com/'
    SMALL_IMAGE = 'avatar_url'
    LARGE_IMAGE = ''

    RESPONSE_ERROR_KEY = 'error'

    def build_api_url(self, url):
        return '%s%s' % (self.GITHUB_API_URL_PREFIX, url)

    def build_api_data(self, **kwargs):
        data = {
            # 'access_token': self.access_token,
        }
        data.update(kwargs)
        return data

    def http_add_header(self, req):
        req.add_header('Accept', 'application/json')
        if hasattr(self, 'access_token'):
            req.add_header('Authorization', 'Token {}'.format(self.access_token))

    def parse_token_response(self, res):
        self.access_token = res['access_token']
        # self.expires_in = res['expires_in']
        # self.refresh_token = res['refresh_token']
        self.token_type = res['token_type']
        res = self.api_call_get('user')

        self.uid = res['id']
        self.name = res['name'] or res['login']
        self.avatar = res['avatar_url']
        self.avatar_large = res['avatar_url']
