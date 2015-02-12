import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_DIR = BASE_DIR

DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = os.path.join(PROJECT_DIR, 'nnpicksdj.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''