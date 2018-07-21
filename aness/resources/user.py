import falcon
from peewee import IntegrityError
from aness.db import pw
from aness.resources import BaseResource


class UserCollectionResource(BaseResource):

    def on_get(self, req, resp):
        model_list = pw.Items().select().first()
        resp.status = falcon.HTTP_200
        resp.media = model_list

    def on_post(self, req, resp):

        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'


class UserResource(BaseResource):

    def on_get(self, req, resp, id):
        resp.status = falcon.HTTP_200
        resp.media = {"id": 2, "firstName": "Julie", "lastName": "Taylor", "managerId": 1, "managerName": "James King",
                      "title": "VP of Marketing", "department": "Marketing", "cellPhone": "617-000-0002",
                      "officePhone": "781-000-0002", "email": "jtaylor@fakemail.com", "city": "Boston, MA",
                      "pic": "julie_taylor.jpg", "twitterId": "@fakejtaylor", "blog": "http://coenraets.org"}

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'
