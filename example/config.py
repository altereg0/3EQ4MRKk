from aumbry import Attr, YamlConfig


class SocialOAuthConfig(YamlConfig):
    __mapping__ = {
    'social_oauth': Attr('social_oauth', dict)
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
        'social_oauth': Attr('social_oauth', list)
    }

    def __init__(self):
        self.db = DatabaseConfig()
        self.gunicorn = {}
        self.social_oauth = []
