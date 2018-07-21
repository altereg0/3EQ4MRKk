from .models import *


# class UnknownField(object):
#     def __init__(self, *_, **__): pass


class PeeweeDBManager(object):
    def __init__(self, connection=None):
        self.connection = connection
        # dynamic initialization
        # database_persistent = SqliteDatabase(self.connection)
        self.db = database_persistent

    @property
    def session(self):
        return self.db.connection_context()

    def setup(self):
        # Normally we would add whatever db setup code we needed here.
        # This will for fine for the ORM
        try:
            self.db.init(self.connection)
            self.db.create_tables([Categories, Items, Images, Pages, Users])
            pass
        except Exception as e:
            print('Could not initialize DB: {}'.format(e))
