import factory

from random import randint
from mimesis import Generic
from mimesis.providers.base import BaseProvider
from mimesis.enums import Gender
from peewee import IntegrityError
from mimesis.schema import Field

from mimesis_factory import MimesisField

from aness.db import models


class AnessCustomProvider(BaseProvider):
    class Meta:
        name = "advertcustom"

    @staticmethod
    def price():
        return randint(100, 100000) / 100


# TODO: Нужно найти более простой и элегантный метод добавления providers в класс
class RUMimesisField(MimesisField):
    _DEFAULT_LOCALE = 'ru'

    def evaluate(self, instance, step, extra):
        """Evaluates the lazy field."""
        if extra is None:
            extra = {}

        kwargs = {}
        kwargs.update(self.kwargs)
        kwargs.update(extra)

        mimesis = self._get_cached_instance(locale=self.locale, field=self.field, **self.kwargs)
        # mimesis = self._get_cached_instance(locale=self.locale)
        kwargs.pop('providers')
        return mimesis(self.field, **kwargs)

    @classmethod
    def _get_cached_instance(cls, locale=None, field=None, **kwargs):
        if locale is None:
            locale = cls._DEFAULT_LOCALE

        _hash = '{:}:{:}'.format(locale, field)

        if _hash not in cls._CACHED_INSTANCES:
            cls._CACHED_INSTANCES[_hash] = Field(locale, **kwargs)

        return cls._CACHED_INSTANCES[_hash]


class ProfilesFactory(factory.Factory):
    class Meta:
        model = models.Users

    name = MimesisField('full_name')
    social = MimesisField('word')
    uid = MimesisField('token')
    # uid = factory.Sequence(lambda n: n),
    email = factory.LazyAttribute(
        lambda o: '%s@example.org' % o.name
    )
    access_token = MimesisField('token', entropy=32)
    fusk = MimesisField('word')


class AdvertsFactory(factory.Factory):
    class Meta:
        model = models.Adverts

    title = MimesisField('title')
    description = MimesisField('text')
    author = factory.SubFactory(ProfilesFactory)
    # uid = factory.Sequence(lambda n: n),
    price = RUMimesisField('advertcustom.price', providers=[AnessCustomProvider])
