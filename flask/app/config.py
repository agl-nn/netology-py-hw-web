from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_V1_URL_PREFIX = '/api/v1/'


class Config(object):
    SQLALCHEMY_DATABASE_URI = f'postgresql://{getenv("DB_USER")}:{getenv("DB_PWD")}@localhost:5432/{getenv("DB_NAME")}'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False