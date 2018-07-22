import falcon
from peewee import IntegrityError
from aness.db import models
from aness.resources import BaseResource
from aness.schemas import UserSchema


class UserCollectionResource(BaseResource):

    def on_get(self, req, resp):
        # with self.db.atomic():
        model_list = models.Users().select()
        userSchema = UserSchema(many=True)
        unresult = userSchema.dump(model_list)
        resp.status = falcon.HTTP_200
        resp.media = unresult.data

    def on_post(self, req, resp):
        userSchema = UserSchema(many=False)
        unresult = userSchema.load(req.media)
        user = unresult.data
        try:
            with self.db.atomic():
                user.save()
        except IntegrityError as e:
            raise falcon.HTTPBadRequest ('Integrity error: {}'.format(e))
        resp.status = falcon.HTTP_201
        resp.media = {'id': user.id}


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
