"""
Module for utils
"""
import importlib
from src.constants import AUDIO_FILE_TYPES


class ValidationSchema:
    """
    Singleton class for getting objects of Marshmallow schema of audio files so that single
    object can be used multiple times.
    """
    _instance = None

    @staticmethod
    def get_instance():
        if ValidationSchema._instance is None:
            ValidationSchema()
        return ValidationSchema._instance

    def __init__(self):
        if ValidationSchema._instance is not None:
            raise Exception("Cannot create new instance because this class is a singleton class.")
        else:
            ValidationSchema._instance = self

            # Generating dict which stores object of marshmallow schemas
            self.validation_schema_objects = {}
            for audio_type in AUDIO_FILE_TYPES:
                class_attributes = get_schema_class(audio_type)
                validator_schema_class = getattr(importlib.import_module("src.routes.serializer"),
                                                 class_attributes["validator"])
                self.validation_schema_objects[audio_type] = {
                    "single": validator_schema_class(),
                    "multiple": validator_schema_class(many=True)
                }

    def get_audio_schema(self, file_type, many=False):
        if not many:
            return self.validation_schema_objects[file_type]["single"]
        return self.validation_schema_objects[file_type]["multiple"]


def get_schema_class(file_type):
    """
    Method for getting class name of marshmallow schema for audio file according to file_type
    """
    res = {
        "validator": f"{str(file_type).capitalize()}Schema"
    }

    return res
