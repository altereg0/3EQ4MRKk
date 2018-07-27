from mimesis.schema import Field, Schema

class BaseResource(object):
    def __init__(self, db_manager):
        self.db = db_manager.database
        self._ = Field('ru')
        self._Schema = Schema


    def generate_mock(self):
        pass