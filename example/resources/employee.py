# -*- coding:utf-8 -*-
import falcon
import json
# from sqlalchemy.exc import IntegrityError
# from example.db import models
from example.resources import BaseResource


# from example.schemas import load_schema

class EmployeeCollectionResource(BaseResource):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        if 'name' in req.params:
            resp.body = json.dumps(
                {"id": 2, "firstName": "Julie", "lastName": "Taylor", "managerId": 1, "managerName": "James King",
                 "title": "VP of Marketing", "department": "Marketing", "cellPhone": "617-000-0002",
                 "officePhone": "781-000-0002", "email": "jtaylor@fakemail.com", "city": "Boston, MA",
                 "pic": "julie_taylor.jpg", "twitterId": "@fakejtaylor", "blog": "http://coenraets.org"}, )

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'


class EmployeeResource(BaseResource):

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
