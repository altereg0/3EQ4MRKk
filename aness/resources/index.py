# -*- coding:utf-8 -*-
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
