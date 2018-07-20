from aumbry import Attr, YamlConfig


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


class AppConfig(YamlConfig):
    __mapping__ = {
        'db': Attr('db', DatabaseConfig),
        'gunicorn': Attr('gunicorn', dict),
        'wsgiref': Attr('wsgiref', dict),
        'social_config': Attr('social_config', SocialOAuthConfig)
    }

    def __init__(self):
        self.db = DatabaseConfig()
        self.gunicorn = {}
        self.social_oauth = {}
