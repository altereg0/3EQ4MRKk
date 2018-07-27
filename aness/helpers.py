from random import randint
from mimesis import Generic
from mimesis.providers.base import BaseProvider
from mimesis.enums import Gender
from functools import wraps
from falcon import HTTPForbidden
from peewee import IntegrityError
from aness.db.models import Users, Adverts


def token_required(func):
    @wraps(func)
    def f(*args, **kwargs):
        resource, req, resp = args
        # if not False:
        #     raise HTTPForbidden
        if not req.context['valid']:
            raise HTTPForbidden
        return func(*args, **kwargs)

    return f


def generate_path(prefix, api_version, resource):
    return '/{prefix:s}/{api:s}/{resource:s}'.format(prefix=prefix, api=api_version, resource=resource)


class AnessCustomProvider(BaseProvider):
    class Meta:
        name = "advertcustom"

    @staticmethod
    def price():
        return randint(100, 100000) / 100


class FuckingFactory(object):

    @staticmethod
    def generate_mock_data(num_users=0, num_adverts=0, locale='ru'):
        if num_adverts > 0 and num_users == 0:
            num_users = 42
        FuckingFactory.generate_mock_data_users(num=num_users, locale=locale)
        FuckingFactory.generate_mock_data_adverts(num=num_adverts, authors=num_users, locale=locale)

    @staticmethod
    def generate_mock_data_users(num=42, locale='ru'):
        gmock = Generic(locale)
        gmocku = Generic('en')

        for _ in range(num):
            _new = Users(
                uid=gmock.cryptographic.token()[:16],
                name=gmock.person.full_name(),
                social=gmocku.text.color().upper()
            )
            try:
                _new.save()
            except IntegrityError as e:
                pass

    @staticmethod
    def generate_mock_data_adverts(num=42, authors=1, locale='ru'):
        gmock = Generic(locale)
        gmock.add_provider(AnessCustomProvider)
        authors = max(1, authors)

        for _ in range(num):
            _new = Adverts(
                title=gmock.text.title(),
                description=gmock.text.text(8),
                user_id=gmock.numbers.between(1, authors),
                price=gmock.advertcustom.price()
            )
            try:
                _new.save()
            except IntegrityError as e:
                pass
