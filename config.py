import os
from .config_example import Config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class ProdConfig(Config):
    SECRET_KEY = 'nh4uG6K9625JNY64gj3kjH574Yn475HNU654kmh768nT7NU6gbf56547gum'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "app.db")}'
