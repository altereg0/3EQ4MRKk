from peewee import *

database_persistent = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = database_persistent


class Categories(BaseModel):
    name = TextField(null=True)
    parent = ForeignKeyField('self', db_column='parent_id', rel_model='self', to_field='id', null=True)
    url = TextField(null=True)

    class Meta:
        db_table = 'categories'


class Items(BaseModel):
    category = ForeignKeyField(Categories, db_column='category_id', null=True, rel_model=Categories, to_field='id')
    description = TextField(null=True)
    details = TextField(null=True)
    item = IntegerField(db_column='item_id')
    timestamp = TimestampField(null=True)
    title = TextField(null=True)
    url = TextField(null=True)
    comment = TextField(null=True)
    active = BooleanField(default=True)
    price = FloatField(default=0.0)

    class Meta:
        db_table = 'items'


class Images(BaseModel):
    filename = TextField(null=True)
    item = ForeignKeyField(Items, db_column='item_id', rel_model=Items, to_field='item')
    path = TextField(null=True)
    status_code = IntegerField(null=True)
    timestamp = TimestampField(null=True)
    url = TextField(null=True)

    class Meta:
        db_table = 'images'


class Pages(BaseModel):
    page_key = TextField(null=True)
    status_code = IntegerField(null=True)
    timestamp = TimestampField(null=True)

    class Meta:
        db_table = 'pages'


class Users(BaseModel):
    name = CharField()
    provider = FixedCharField(8)
    uid = CharField(16)

    class Meta:
        db_table = 'users'

# class SqliteSequence(BaseModel):
#     name = UnknownField(null=True)  #
#     seq = UnknownField(null=True)  #
#
#     class Meta:
#         db_table = 'sqlite_sequence'
#         primary_key = False
