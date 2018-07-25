from peewee import *

# db = SqliteDatabase(None)
db = Proxy()


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    name = CharField()
    provider = FixedCharField(8)
    uid = CharField(16)

    # class Meta:
    #     db_table = 'users'


class Categories(BaseModel):
    name = TextField(null=True)
    parent = ForeignKeyField('self', db_column='parent_id', rel_model='self', to_field='id', null=True)
    url = TextField(null=True)

    # class Meta:
    #     db_table = 'categories'


class Adverts(BaseModel):
    title = TextField(null=True)
    description = TextField(null=True)
    timestamp = TimestampField(null=True)
    url = TextField(null=True)
    active = BooleanField(default=True)
    price = FloatField(default=0.0)
    author = ForeignKeyField(Users, db_column='user_id', null=False, rel_model=Users, to_field='id')
    #
    # class Meta:
    #     db_table = 'items'


class Images(BaseModel):
    status_code = IntegerField(null=True)
    timestamp = TimestampField(null=True)
    url = TextField(null=True)

    # class Meta:
    #     db_table = 'images'


class Pages(BaseModel):
    page_key = TextField(null=True)
    status_code = IntegerField(null=True)
    timestamp = TimestampField(null=True)

    # class Meta:
    #     db_table = 'pages'

MODELS = (Categories, Adverts, Images, Pages, Users)
