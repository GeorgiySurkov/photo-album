import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class DevConfig:
    SECRET_KEY = 'you_will never_guess'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, os.path.normpath('media'))
