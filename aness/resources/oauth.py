# -*- coding:utf-8 -*-

import os
import sys
import falcon
from string import Template

from aness.resources import BaseResource

from peewee import IntegrityError
from socialoauth import SocialSites
from socialoauth.exception import SocialAPIError
# from aness.helpers import generate_user_token
from aness.schemas import UserSchema
from aness.db.models import Users

from marshmallow_jsonapi import fields, Schema

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.normpath(os.path.join(CURRENT_PATH, '..')))

IMAGE_PATH = os.path.join(CURRENT_PATH, 'images')


# SUCCESS_TPL = '<!DOCTYPE html><html><head><script type="text/javascript">localStorage.setItem("application.token", {"foo":"$token"}); window._foo = "bar"; window.close();</script></head><body></body></html>'
# SUCCESS_TPL = '<!DOCTYPE html><html><head><script type="text/javascript">window._token="$token"; window.close();</script></head><body></body></html>'


class OAuthBaseResource(BaseResource):
    def __init__(self, db_manager, cfg):
        super(OAuthBaseResource, self).__init__(db_manager)
        # patch url
        self.social_sites = SocialSites(cfg.sites_list)
        self.base_url = cfg.base_url


class OAuthResource(OAuthBaseResource):

    def _link(self, site_class):
        _s = self.social_sites.get_site_object_by_class(site_class)
        if os.path.exists(os.path.join(IMAGE_PATH, _s.site_name + '.png')):
            # TODO Добавить путь к пиктограмме OAuth сервиса
            pass

        return dict(id=_s.ID, name=_s.site_name, title=_s.site_name_zh, url=_s.authorize_url)

    def on_get(self, req, resp):
        links = tuple(map(self._link, self.social_sites.list_sites_class()))
        oauth_schema = OAuthEntitySchema()
        unresult = oauth_schema.format_json_api_response(links, True)
        resp.status = falcon.HTTP_200
        resp.media = unresult


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
        # Ищем пользователя
        userSchema = UserSchema(many=False)
        user = Users.get_or_none(Users.uid == '{}'.format(s.uid), Users.provider == provider)
        if user is None:
            mock = {
                'data': {
                    'type': 'user',
                    'attributes': {
                        'provider': provider, 'name': s.name, 'uid': '{}'.format(s.uid)
                    }
                }
            }
            unresult = userSchema.load(mock, many=False)
            user = unresult.data
            try:
                with self.db.atomic():
                    user.save()
            except IntegrityError as e:
                raise falcon.HTTPBadRequest('User creation error', 'Cannot save user in database')

        # token = generate_user_token(user).decode()
        userDump = userSchema.dump(user)
        resp.context.update({'user': userDump.data})
        # resp.status = falcon.HTTP_OK
        # resp.content_type = falcon.MEDIA_HTML
        # resp.body = Template(SUCCESS_TPL).substitute(token=token)


class OAuthEntitySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    title = fields.Str()
    url = fields.Str()

    class Meta:
        type_ = 'oauth'
        strict = False
