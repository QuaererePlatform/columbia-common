__all__ = ['CCDataSchema', 'CCIndexesSchema', 'CCScansSchema']

from marshmallow import fields
from quaerere_base_common.schema import BaseSchema

from ..models import CCDataBase, CCIndexesBase, CCScansBase


class CCDataSchema(BaseSchema, CCDataBase):
    _key = fields.String()


class CCIndexesSchema(BaseSchema, CCIndexesBase):
    _key = fields.String()


class CCScansSchema(BaseSchema, CCScansBase):
    _key = fields.String()
