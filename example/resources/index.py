# -*- coding:utf-8 -*-
import falcon

from sqlalchemy.exc import IntegrityError

from example.db import models
from example.resources import BaseResource
from example.schemas import load_schema

class IndexResource(BaseResource):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works! Mememe Plus reload '

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'
