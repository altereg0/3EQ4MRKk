# -*- coding:utf-8 -*-
import falcon
import json


class EmployeeCollectionResource(object):
    def __init__(self):
        pass

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        if 'name' in req.params:
            resp.body = json.dumps(
                {"id": 2, "firstName": "Julie", "lastName": "Taylor", "managerId": 1, "managerName": "James King",
                 "title": "VP of Marketing", "department": "Marketing", "cellPhone": "617-000-0002",
                 "officePhone": "781-000-0002", "email": "jtaylor@fakemail.com", "city": "Boston, MA",
                 "pic": "julie_taylor.jpg", "twitterId": "@fakejtaylor", "blog": "http://coenraets.org"},)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'


class EmployeeResource(object):
    def __init__(self):
        pass

    def on_get(self, req, resp, id):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(
            {"id": 2, "firstName": "Julie", "lastName": "Taylor", "managerId": 1, "managerName": "James King",
             "title": "VP of Marketing", "department": "Marketing", "cellPhone": "617-000-0002",
             "officePhone": "781-000-0002", "email": "jtaylor@fakemail.com", "city": "Boston, MA",
             "pic": "julie_taylor.jpg", "twitterId": "@fakejtaylor", "blog": "http://coenraets.org"},)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'
