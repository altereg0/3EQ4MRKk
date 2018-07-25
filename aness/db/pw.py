from .models import MODELS, db
from peewee import SqliteDatabase


# class UnknownField(object):
#     def __init__(self, *_, **__): pass


class PeeweeDBManager(object):
    def __init__(self, connection=None):
        self.connection = connection
        # proxy initialization
        self.database = SqliteDatabase(self.connection,
                                       # thread_safe=False,
                                       # check_same_thread=False,
                                       pragmas={
                                           'journal_mode': 'wal',
                                           'cache_size': -1 * 64000,  # 64MB
                                           'foreign_keys': 1,
                                           'ignore_check_constraints': 0,
                                           'synchronous': 0}
                                       )
        db.initialize(self.database)
        # dynamic initialization
        # db.init(self.connection)
        # db = connect(self.connection)
        # self.database = db

    @property
    def session(self):
        return self.database.connection_context

    def setup(self):
        # Normally we would add whatever db setup code we needed here.
        # This will for fine for the ORM
        try:
            self.database.create_tables(MODELS, safe=True)
        except Exception as e:
            print('Could not initialize DB: {}'.format(e))
