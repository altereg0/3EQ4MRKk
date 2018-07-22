# -*- coding:utf-8 -*-

import os
import sys
import json
import falcon
from string import Template

from aness.db import models
from aness.resources import BaseResource
from aness.schemas import UserSchema

from aness.db.models import Users
from peewee import IntegrityError
from socialoauth import SocialSites
from socialoauth.exception import SocialAPIError
from aness.helpers import generate_user_token
from aness.schemas import UserSchema

from marshmallow_jsonapi import fields, Schema

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.normpath(os.path.join(CURRENT_PATH, '..')))

IMAGE_PATH = os.path.join(CURRENT_PATH, 'images')

SUCCESS_TPL = '<!DOCTYPE html><html><head><script type="text/javascript">localStorage.setItem("token", "$token"); window.close();</script></head><body></body></html>'


class OAuthBaseResource(BaseResource):
    def __init__(self, db_manager, cfg):
        super(OAuthBaseResource, self).__init__(db_manager)
        # patch url
        self.social_sites = SocialSites(cfg.sites_list)
        self.base_url = cfg.base_url
        self.schema = UserSchema()


class OAuthResource(OAuthBaseResource):

    def _link(self, site_class):
        _s = self.social_sites.get_site_object_by_class(site_class)
        if os.path.exists(os.path.join(IMAGE_PATH, _s.site_name + '.png')):
            # TODO Добавить путь к пиктограмме OAuth сервиса
            pass

        return dict(id=_s.ID, name=_s.site_name, title=_s.site_name_zh, url=_s.authorize_url)

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        # resp.body = 'Server works! Mememe Plus reload '
        links = tuple(map(self._link, self.social_sites.list_sites_class()))
        # mimetypes.common_types.html
        oauth_schema = OAuthEntitySchema()
        resp.body = json.dumps(oauth_schema.format_json_api_response(links, True))

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Server works!'


class CallbackResource(OAuthBaseResource):
    def on_get(self, req, resp, provider):
        code = req.params.get('code')
        if not code:
            # error occurred
            challenges = ['Digest']
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')
            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

        socialsites = SocialSites(self.social_sites)
        s = socialsites.get_site_object_by_name(provider)
        try:
            s.get_access_token(code)
        except SocialAPIError as e:
            challenges = ['Digest']
            description = '{} {} {}'.format(e.site_name, e.url, e.error_msg)
            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

        # retrive and store: uid, name, avatar...
        # storage = UserStorage()
        # UID = storage.get_uid(s.site_name, s.uid)
        # if not UID:
        #     UID = storage.bind_new_user(s.site_name, s.uid)
        #
        # storage.set_user(UID, site_name=s.site_name, uid=s.uid, name=s.name, avatar=s.avatar)
        try:
            unresult = self.schema.load(data={'provider': provider, 'name': s.name, 'uid': s.uid}, many=False)
            user = unresult.data
            with self.db.atomic():
                user.save()
        except IntegrityError as e:
            raise falcon.HTTPBadRequest('User creation error', 'Cannot save user in database')

        token = generate_user_token(user).decode()
        resp.status = falcon.HTTP_OK
        resp.content_type = 'text/html'
        resp.body = Template(SUCCESS_TPL).substitute(token=token)


class OAuthEntitySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    title = fields.Str()
    url = fields.Str()

    class Meta:
        type_ = 'oauth'
        strict = False
