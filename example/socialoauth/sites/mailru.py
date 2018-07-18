# -*- coding: utf-8 -*-

from app.socialoauth.sites.base import OAuth2


class MailRu(OAuth2):
    ID = 'b0oib4yp'
    AUTHORIZE_URL = 'https://connect.mail.ru/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://connect.mail.ru/oauth/token'

    MAILRU_API_URL_PREFIX = 'https://connect.mail.ru/'
    SMALL_IMAGE = 'avatar_url'
    LARGE_IMAGE = ''

    RESPONSE_TYPE = 'code'
    """
    code — используйте если вам нужен доступ к API и данным пользователя только с серверной части вашего сайта
    token — используйте, если вам нужен доступ к API только из JavaScript, например, если у вас веб-приложение, полностью работающее внутри браузера пользователя
    code_and_token — если вам нужен доступ к API и из серверной части сайта, и из JavaScript, используйте этот вариант
    """

    RESPONSE_ERROR_KEY = 'error'

    def build_api_url(self, url):
        return '%s%s' % (self.ACCESS_TOKEN_URL, url)

    def build_api_data(self, **kwargs):
        data = {
            # 'client_id': self.access_token,
            # 'client_secret': self.cli,
            # 'grant_type': 'authorization_code'
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
        res = self.api_call_post()

        self.uid = res['id']
        self.name = res['name']
        self.avatar = res['avatar_url']
        self.avatar_large = res['avatar_url']
