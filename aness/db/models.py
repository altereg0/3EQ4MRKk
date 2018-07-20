import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

SAModel = declarative_base()


class UserModel(SAModel):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(128), unique=True)
    provider = sa.Column(sa.String(128))
    provider_id = sa.Column(sa.Integer)
    score = sa.Column(sa.Integer)

    def __init__(self, username, provider, score):
        # super(UserModel, self).__init__()
        self.username = username
        self.provider = provider
        self.score = score

    @property
    def as_dict(self):
        return {
            'username': self.username,
            'provider': self.provider,
            'score': self.score
        }

    def save(self, session):
        with session.begin():
            session.add(self)

    @classmethod
    def get_list(cls, session):
        models = []

        with session.begin():
            query = session.query(cls)
            models = query.all()

        return models


class MessageModel(SAModel):
    __tablename__ = 'messages'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    message = sa.Column(sa.String(128))
    timestamp = sa.Column(sa.Integer)

    def __init__(self, user_id, message):
        # super(MesageModel, self).__init__()
        self.user_id = user_id
        self.message = message

    @property
    def as_dict(self):
        return {
            'author': self.user_id,
            'message': self.message
        }

    def save(self, session):
        with session.begin():
            session.add(self)

    @classmethod
    def get_list(cls, session):
        models = []

        with session.begin():
            query = session.query(cls)
            models = query.all()

        return models
