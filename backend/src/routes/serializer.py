"""
Module for serializer
"""
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class SongSchema(Schema):
    """
    Class for schema of Song with validation constraints
    """
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True, validate=[
        Length(min=1, max=100, error="name length must be between 1 to 100"),
    ])
    duration = fields.Integer(required=True, validate=Range(min=1, error="duration must be greater than 0"))
    uploaded_time = fields.DateTime(dump_only=True)


class PodcastSchema(Schema):
    """
    Class for schema of Podcast with validation constraints
    """
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True, validate=[
        Length(min=1, max=100, error="name length must be between 1 to 100"),
    ])
    duration = fields.Integer(required=True, validate=Range(min=1, error="duration must be greater than 0"))
    host = fields.Str(required=True, validate=[
        Length(min=1, max=100, error="name length must be between 1 to 100"),
    ])
    participants = fields.List(fields.String(validate=Length(min=1, max=100)), required=False,
                               validate=Length(max=10))
    uploaded_time = fields.DateTime(dump_only=True)


class AudiobookSchema(Schema):
    """
    Class for schema of Audiobook with validation constraints
    """
    id = fields.Integer(dump_only=True)
    title = fields.Str(required=True, validate=[
        Length(min=1, max=100, error="title length must be between 1 to 100"),
    ])
    author = fields.Str(required=True, validate=[
        Length(min=1, max=100, error="author length must be between 1 to 100"),
    ])
    narrator = fields.Str(required=True, validate=[
        Length(min=1, max=100, error="narrator length must be between 1 to 100"),
    ])
    duration = fields.Integer(required=True, validate=Range(min=1, error="duration must be greater than 0"))
    uploaded_time = fields.DateTime(dump_only=True)
