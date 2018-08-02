from random import randint
from functools import wraps

from falcon import HTTPForbidden

from aness.factories import ProfilesFactory, AdvertsFactory

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


class FuckingFactory(object):

    @staticmethod
    def generate_mock_data(num_users=1, num_max_adverts_per_user=5, locale='ru'):
        for _user_iter in range(num_users):
            user = ProfilesFactory.build()
            user.save()
            for _advert_iter in range(randint(1,num_max_adverts_per_user)):
                advert = AdvertsFactory.create()
                advert.author = user
                advert.save()

