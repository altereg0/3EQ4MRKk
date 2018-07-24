import falcon
from peewee import *

# Пример из http://docs.peewee-orm.com/en/latest/peewee/database.html#recommended-settings
class PeeweeConnectionMiddleware(object):
    def __init__(self):
        self.db = SqliteDatabase(None)

    def process_request(self, req, resp):
        self.db.connect(reuse_if_open=True)

    def process_response(self, req, resp, resource):
        # TODO: Проблема БД с типом :memory:
        # они существуют только в пределах создавшего thread
        # и при закрытии обнуляются
        if not self.db.is_closed():
            if self.db.database != ":memory:":
                self.db.close()

    def setup_database(self, db):
        self.db = db
