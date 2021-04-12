import os
from flask import Flask
from flask_cors import CORS
from sqlalchemy_utils import create_database, database_exists

from src.config import config_by_name


app = Flask(__name__)
app.config.from_object(config_by_name[os.environ['APP_ENV']])
CORS(app)
database_uri = app.config['SQLALCHEMY_DATABASE_URI']
if not database_exists(database_uri):
    create_database(database_uri)


