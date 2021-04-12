"""
Module for DB Operations
"""
import importlib

from .db_connection import DBConnection

db = DBConnection.get_instance().get_db_instance()
module = importlib.import_module("src.routes.models")


def add_audio_file(data, model_class):
    """
    Module for inserting data into song/podcast/audiobook table according to the model_class.

    :param data: dict of data to be inserted
    :param model_class: Name of the model Class e.g, Song/Podcast/Audiobook

    :returns model object of inserted data
    """
    audio = getattr(module, model_class)(**data)
    db.session.add(audio)
    db.session.commit()
    return audio


def update_audio_file(file_id, data, model_class):
    """
    Module for updating data into song/podcast/audiobook table according to the model_class.

    :param file_id: id for which data needs to be updated
    :param data: dict of data to be updated
    :param model_class: Name of the model Class e.g, Song/Podcast/Audiobook
    """
    audio_model_class = getattr(module, model_class)

    audio = db.session.query(audio_model_class).get(file_id)
    if audio is None:
        return False
    for field, value in data.items():
        setattr(audio, field, value)
    db.session.commit()
    return True


def delete_audio_file(file_id, model_class):
    """
    Module for deleting data into song/podcast/audiobook table according to the model_class.

    :param file_id: id for which data needs to be deleted
    :param model_class: Name of the model Class e.g, Song/Podcast/Audiobook
    """
    audio_model_class = getattr(module, model_class)

    audio = db.session.query(audio_model_class).get(file_id)
    if audio is None:
        return False
    db.session.delete(audio)
    db.session.commit()
    return True


def get_audio_files(file_id, model_class):
    """
    Module for retrieving data from song/podcast/audiobook table according to the model_class.

    :param file_id: id for which data needs to be retrieved
    :param model_class: Name of the model Class e.g, Song/Podcast/Audiobook
    """
    audio_model_class = getattr(module, model_class)

    # If file_id is None then fetching all the records
    filter_query = {"id": file_id} if file_id is not None else {}

    audio = audio_model_class.query.filter_by(**filter_query).all()
    if audio is None:
        return []
    return audio

