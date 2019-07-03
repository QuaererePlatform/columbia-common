__all__ = ['CCDataBase', 'CCIndexesBase', 'CCScansBase']

from marshmallow import fields


class CCDataBase:
    url_key = fields.String(required=True)
    timestamp = fields.String(required=True)
    url = fields.Url(required=True)
    status = fields.String(required=True)
    filename = fields.String(required=True)
    offset = fields.String()
    digest = fields.String()
    length = fields.String()
    mime = fields.String()
    mime_detected = fields.String()
    charset = fields.String()
    languages = fields.String()


class CCIndexesBase:
    id = fields.String(required=True)
    name = fields.String(required=True)
    timegate = fields.Url(required=True)
    cdx_api = fields.Url(required=True)


class CCScansBase:
    pass
