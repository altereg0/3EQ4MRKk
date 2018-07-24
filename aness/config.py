from aumbry import Attr, YamlConfig
from datetime import timedelta


class SocialOAuthConfig(YamlConfig):
    __mapping__ = {
        'sites_list': Attr('sites_list', list),
        'base_url': Attr('base_url', str)
    }


class DatabaseConfig(YamlConfig):
    __mapping__ = {
        'connection': Attr('connection', str),
    }
    connection = ''


class DatabaseWrapperConfig(YamlConfig):
    __mapping__ = {
        'sa': Attr('sa', DatabaseConfig),
        'pw': Attr('pw', DatabaseConfig),
    }
    connection = ''


class SecurityConfig(YamlConfig):
    __mapping__ = {
        'token_prefix': Attr('token_prefix', str),
        'token_expiry': Attr('token_expiry', int),
        'tokens_leeway': Attr('tokens_leeway', int),
        'tokens_authorize_endpoint': Attr('tokens_authorize_endpoint', str),
        'tokens_refresh_endpoint': Attr('tokens_refresh_endpoint', str),
        'tokens_enable_refresh': Attr('tokens_enable_refresh', bool),
        'secret': Attr('secret', str),
    }
    secret = 'secret'
    token_prefix = 'JWT'
    token_expiry = timedelta(hours=1)
    tokens_leeway = timedelta(seconds=0)
    tokens_enable_refresh = False


class AppConfig(YamlConfig):
    __mapping__ = {
        'db': Attr('db', DatabaseWrapperConfig),
        'gunicorn': Attr('gunicorn', dict),
        'wsgiref': Attr('wsgiref', dict),
        'social_config': Attr('social_config', SocialOAuthConfig),
        'security': Attr('security', SecurityConfig)
    }

    def __init__(self):
        self.db = DatabaseConfig()
        self.gunicorn = {}
        self.social_oauth = {}
