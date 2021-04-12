"""
Module for routes
"""
from flask import request, jsonify
import logging
from ..db_utils.db_operations import add_audio_file, update_audio_file, delete_audio_file, get_audio_files
from src.app import app
from src.constants import AUDIO_FILE_TYPES
from src.utils import ValidationSchema

logger = logging.getLogger("AUDIO_ROUTE")
validation_schema_instance = ValidationSchema.get_instance()


@app.route('/api/v1/audioFile/<file_type>', methods=['POST'])
def handle_create_audio_file(file_type):
    """
    route for POST API for all types of audio file
    :param file_type: file type
    """
    try:
        # Checking file type received is correct or not
        if file_type not in AUDIO_FILE_TYPES:
            return f"{file_type} file type not supported", 400
        data = request.get_json(force=True, silent=True)
        if data is None:
            return "Invalid JSON Data", 400

        # Getting model class name from file type
        model_class = str(file_type).capitalize()

        # Dynamically getting object of validator schema according to file_type
        validator = validation_schema_instance.get_audio_schema(file_type, many=False)
        errors = validator.validate(data)
        if errors:
            return jsonify(errors), 400

        # Creating resource
        audio = add_audio_file(data, model_class)

        # Serializing the data
        res = validator.dumps(audio)
        return res, 200
    except Exception as e:
        message = f"ERROR: Exception occurred in creating audio file: {str(e)}"
        logger.error(message)
        return message, 500


@app.route('/api/v1/audioFile/<file_type>/<int:file_id>', methods=['PUT'])
def handle_update_audio_file(file_type, file_id):
    """
    route for PUT API for all types of audio file
    :param file_type: file type
    :param file_id: file id
    """
    try:
        # Checking file type received is correct or not
        if file_type not in AUDIO_FILE_TYPES:
            return f"{file_type} file type not supported", 400

        data = request.get_json(force=True, silent=True)
        if data is None:
            return "Invalid JSON Data", 400
        elif not bool(data):
            return "Provide at least one field for update", 400

        # Getting model class name from file type
        model_class = str(file_type).capitalize()

        # Dynamically getting object of validator schema according to file_type
        validator = validation_schema_instance.get_audio_schema(file_type, many=False)
        errors = validator.validate(data, partial=True)
        if errors:
            return jsonify(errors), 400

        # Updating the resource
        update_status = update_audio_file(file_id, data, model_class)
        if not update_status:
            return f"{file_type} with id {file_id} not found", 404
        return f"{file_type} with id {file_id} updated successfully.", 200
    except Exception as e:
        message = f"ERROR: Exception occurred in updating audio file: {str(e)}"
        logger.error(message)
        return message, 500


@app.route('/api/v1/audioFile/<file_type>/<int:file_id>', methods=['DELETE'])
def handle_delete_audio_file(file_type, file_id):
    """
    route for DELETE API for all types of audio file
    :param file_type: file type
    :param file_id: file id
    """
    try:
        # Checking file type received is correct or not
        if file_type not in AUDIO_FILE_TYPES:
            return f"{file_type} file type not supported", 400

        # Getting model class name from file type
        model_class = str(file_type).capitalize()

        # Deleting the resource
        delete_status = delete_audio_file(file_id, model_class)
        if not delete_status:
            return f"{file_type} with id {file_id} not found", 404
        return f"{file_type} with id {file_id} deleted successfully.", 200
    except Exception as e:
        message = f"ERROR: Exception occurred in deleting audio file: {str(e)}"
        logger.error(message)
        return "message", 500


@app.route('/api/v1/audioFile/<file_type>', methods=['GET'])
@app.route('/api/v1/audioFile/<file_type>/<int:file_id>', methods=['GET'])
def handle_get_audio_file(file_type, file_id=None):
    """
    route for GET API for all types of audio file both with specific id and all records
    :param file_type: file type
    :param file_id: file id
    """
    try:
        # Checking file type received is correct or not
        if file_type not in AUDIO_FILE_TYPES:
            return f"{file_type} file type not supported", 400

        # Getting model class name from file type
        model_class = str(file_type).capitalize()

        # Dynamically getting object of validator schema according to file_type
        validator = validation_schema_instance.get_audio_schema(file_type, many=True)

        # Fetching data
        audio_record = get_audio_files(file_id, model_class)
        if (not audio_record) and (file_id is not None):
            return f"{file_type} with id {file_id} not found", 404

        # Serializing the data
        res = validator.dumps(audio_record)
        return res, 200
    except Exception as e:
        message = f"ERROR: Exception occurred in fetching audio file: {str(e)}"
        logger.error(message)
        return message, 500

