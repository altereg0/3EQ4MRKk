import falcon
from aness.resources import BaseResource
from aness.schemas import IndexSchema


class IndexResource(BaseResource):

    def on_get(self, req, resp):
        obj = {
            'id': req.context['request_id'],
            'document_meta': {
                'copyright': 'Nocopyright',
                "authors": [
                    "altereg0"
                ]
            }
        }
        _schema = IndexSchema()
        unresult = _schema.dump(obj)
        resp.status = falcon.HTTP_200
        resp.media = unresult.data


    def generate_mock(self):
        _ = self._
        description = (
            lambda: {
                "id": _('uuid'),
                "name": _('word'),
                "version": _('version', pre_release=True),
                "owner": {
                    "email": _('email', key=str.lower),
                    "token": _('token'),
                    "creator": _('full_name'),
                },
            }
        )
        schema = self._Schema(schema=description)
        j = schema.create(iterations=1)
        pass
