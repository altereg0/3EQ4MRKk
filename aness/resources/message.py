# -*- coding:utf-8 -*-
from time import sleep
import falcon
import json
# from aness.db.models import MessageModel
# from sqlalchemy.exc import IntegrityError
# from aness.db import models
from aness.resources import BaseResource
# from aness.schemas import load_schema


class MessageCollectionResource(BaseResource):

    def on_get(self, req, resp):
        # m = self.model.get_all()
        m = ({"id": 1, "title": "Julie", "content": "jtaylor@fakemail.com", "city": "Boston, MA"},
             {"id": 4, "title": "Bravo", "content": "bravo@fakemail.com", "city": "Boston, MA"},
             {"id": 5, "title": "Charlie", "content": "charlie@fakemail.com", "city": "Boston, MA"},
             )
        resp.status = falcon.HTTP_200
        # resp.body = self.model.schema.dumps(m, many=True).data
        resp.body = json.dumps(m)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        sleep(3)
        resp.body = "Nothing"


class MessageResource(BaseResource):

    def on_get(self, req, resp, id):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(
            {"id": 2, "firstName": "Julie", "lastName": "Taylor", "managerId": 1, "managerName": "James King",
             "title": "VP of Marketing", "department": "Marketing", "cellPhone": "617-000-0002",
             "officePhone": "781-000-0002", "email": "jtaylor@fakemail.com", "city": "Boston, MA",
             "pic": "julie_taylor.jpg", "twitterId": "@fakejtaylor", "blog": "http://coenraets.org"}, )

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'