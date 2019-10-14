from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import ProdConfig, BASE_DIR
from PIL import Image
import warnings
import os
from os import path

warnings.simplefilter('error', Image.DecompressionBombWarning)

app = Flask(__name__)
app.config.from_object(ProdConfig)

if not path.exists(path.join(BASE_DIR, 'media')):
    os.mkdir(path.join(path.join(BASE_DIR, 'media')))
if not path.exists(path.join(BASE_DIR, 'media', 'images')):
    os.mkdir(path.join(path.join(BASE_DIR, 'media', 'images')))
if not path.exists(path.join(BASE_DIR, 'media', 'thumbnails')):
    os.mkdir(path.join(path.join(BASE_DIR, 'media', 'thumbnails')))


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
