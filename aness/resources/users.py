import falcon
from peewee import IntegrityError
from aness.db import models
from aness.resources import BaseResource
from aness.schemas import UserSchema

from aness.helpers import token_required


class UserCollectionResource(BaseResource):

    def on_get(self, req, resp):
        # with self.db.atomic():
        model_list = models.Users().select()
        _schema = UserSchema(many=True)
        unresult = _schema.dump(model_list)
        resp.status = falcon.HTTP_200
        resp.media = unresult.data

    def on_post(self, req, resp):
        _schema = UserSchema(many=False)
        unresult = _schema.load(req.media)
        user = unresult.data
        try:
            with self.db.atomic():
                user.save()
        except IntegrityError as e:
            raise falcon.HTTPBadRequest('Integrity error: {}'.format(e))
        resp.status = falcon.HTTP_201
        resp.media = {'id': user.id}


class UserResource(BaseResource):

    @token_required
    def on_get(self, req, resp, id):
        model_list = models.Users.get_or_none(models.Users.id == id)
        _schema = UserSchema(many=False)
        unresult = _schema.dump(model_list)
        resp.status = falcon.HTTP_200
        resp.media = unresult.data

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'
