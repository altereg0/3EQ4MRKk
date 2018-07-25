from datetime import datetime, tzinfo, timedelta
from pathlib import Path
from urllib.parse import urlunparse

from marshmallow import post_load
from marshmallow_jsonapi import Schema, fields

from marshmallow.validate import Range

from aness.db.models import Users, Adverts

hostname = 'etagy.retla.net'


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    provider = fields.String()
    uid = fields.String()

    class Meta:
        type_ = 'user'
        strict = False

    @post_load
    def make_user(self, data):
        return Users(**data)


class GMT3(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=3) + self.dst(dt)

    def dst(self, dt):
        d = datetime(dt.year, 4, 1)
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)

    def tzname(self, dt):
        return "GMT +3 Moscow"


class OlxImageFileName(fields.Field):
    def _serialize(self, value, attr, obj):
        ret = Path(value)
        return ret.name


class OlxTimeStampConverted(fields.Field):
    def _serialize(self, value, attr, obj):
        ret = value.strftime('%Y%m%d%H%M%S')
        return ret


class ImageSchema(Schema):
    src = fields.Url()

    class Meta:
        type_ = 'image'
        additional = ('id',)

    def OlxImageUrlConverted(self, obj):
        _file = Path(obj.filename)
        ret = urlunparse(
            ('https', hostname, 'images/{:}/{:}'.format(_file.parent.name, _file.name), None, None, None))
        return ret


class AdvertSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    images_set = fields.Relationship(schema=ImageSchema, many=True, dump_only=True, dump_to='images')
    description = fields.String()
    author = fields.Relationship(schema=UserSchema,
                                 type_='user',
                                 related_url='/users/{author_id}',
                                 related_url_kwargs={'author_id': '<author.id>'},
                                 include_resource_linkage=False)
    # timestamp = OlxTimeStampConverted()
    timestamp = fields.LocalDateTime('%Y%m%d%H%M%S', dump_only=True)
    key = fields.Method('ExampleKeyGenerated', dump_only=True)

    class Meta:
        type_ = 'advert'
        additional = ('id',)

    def ExampleKeyGenerated(self, obj):
        return ''.join(('@', str(obj.item)))

    @post_load
    def make_advert(self, data):
        return Adverts(**data)
