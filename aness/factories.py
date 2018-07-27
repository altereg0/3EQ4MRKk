import factory
from mimesis_factory import MimesisField

from aness.db.models import Users

class AccountFactory(factory.Factory):
    class Meta:
        model = Users

    name = MimesisField('name',)
    provider = MimesisField('word'),
    uid = MimesisField('token'),
    # uid = factory.Sequence(lambda n: n),
    email = factory.LazyAttribute(
        lambda o: '%s@example.org' % o.name
    )
    access_token = MimesisField('token', entropy=32)