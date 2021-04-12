"""
Module for DB Models
"""
from ..db_utils.db_connection import DBConnection
from datetime import datetime

db = DBConnection.get_instance().get_db_instance()


class Song(db.Model):
    """
    Model class for song table
    """
    __tablename__ = "song"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)


class Podcast(db.Model):
    """
    Model class for podcast table
    """
    __tablename__ = "podcast"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.JSON, nullable=True, default=[])
    uploaded_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)


class Audiobook(db.Model):
    """
    Model class for audiobook table
    """
    __tablename__ = "audiobook"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
