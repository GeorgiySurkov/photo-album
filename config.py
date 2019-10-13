import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, os.path.normpath('media'))


class ProdConfig(Config):
    SECRET_KEY = 'nh4uG6K9625JNY64gj3kjH574Yn475HNU654kmh768nT7NU6gbf56547gum'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "app.db")}'
