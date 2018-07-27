import factory
from mimesis_factory import MimesisField

from aness.db import models

class RU(MimesisField):
    _DEFAULT_LOCALE = 'ru'

class AccountFactory(factory.Factory):
    class Meta:
        model = models.Users

    name = RU('name')
    social = RU('word')
    uid = MimesisField('token')
    # uid = factory.Sequence(lambda n: n),
    email = factory.LazyAttribute(
        lambda o: '%s@example.org' % o.name
    )
    access_token = MimesisField('token', entropy=32)
    fusk = RU('word')
