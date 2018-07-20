# -*- coding:utf-8 -*-
import falcon

# from sqlalchemy.exc import IntegrityError
# from aness.db import models
from aness.resources import BaseResource
# from aness.schemas import load_schema

class IndexResource(BaseResource):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'
