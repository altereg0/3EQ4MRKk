# -*- coding:utf-8 -*-
from time import sleep
import falcon
import json
from peewee import IntegrityError
from aness.db import models
from aness.resources import BaseResource
from aness.schemas import AdvertSchema


class AdvertsCollectionResource(BaseResource):

    def on_get(self, req, resp):
        model_list = models.Adverts().select()
        _schema = AdvertSchema(many=True)
        unresult = _schema.dump(model_list)
        resp.status = falcon.HTTP_200
        resp.media = unresult.data

    def on_post(self, req, resp):
        _schema = AdvertSchema(many=False)
        _media = req.media
        unresult = _schema.load(_media)
        advert = unresult.data

        try:
            with self.db.atomic():
                # advert = models.Adverts.create(title='Title', description='Any', user_id='2')
                advert.save()
        except IntegrityError as e:
            raise falcon.HTTPBadRequest('Integrity error: {}'.format(e))
        resp.status = falcon.HTTP_201
        resp.media = {'id': advert.id}


class AdvertsResource(BaseResource):

    def on_get(self, req, resp, id):
        model_list = models.Adverts.get_or_none(models.Adverts.id == id)
        _schema = AdvertSchema(many=False)
        unresult = _schema.dump(model_list)
        resp.status = falcon.HTTP_200
        resp.media = unresult.data

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'
