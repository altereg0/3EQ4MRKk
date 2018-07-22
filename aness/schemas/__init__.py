from datetime import datetime, tzinfo, timedelta
from pathlib import Path
from urllib.parse import urlunparse

from marshmallow import post_load
from marshmallow_jsonapi import Schema, fields

from marshmallow.validate import Range

from aness.db.models import Users

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
        # return Users.create(**data)


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


class OlxImageSchema(Schema):
    filename = OlxImageFileName()
    url = fields.Url()
    loc = fields.Method('OlxImageUrlConverted', dump_only=True)

    class Meta:
        additional = ('id',)

    def OlxImageUrlConverted(self, obj):
        _file = ret = Path(obj.filename)
        ret = urlunparse(
            ('http', hostname, 'images/{:}/{:}'.format(_file.parent.name, _file.name), None, None, None))
        return ret


class OlxItemSchema(Schema):
    item = fields.Integer(dump_only=True)
    images_set = fields.Nested(OlxImageSchema, many=True, dump_only=True, dump_to='images')
    url = fields.Url()
    title = fields.String()
    description = fields.String()
    details = fields.String()
    # timestamp = OlxTimeStampConverted()
    timestamp = fields.LocalDateTime('%Y%m%d%H%M%S')
    key = fields.Method('OlxKeyGenerated')

    class Meta:
        additional = ('id',)

    def OlxKeyGenerated(self, obj):
        return ''.join(('olx', str(obj.item)))
