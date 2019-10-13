from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import ProdConfig
from PIL import Image
import warnings

warnings.simplefilter('error', Image.DecompressionBombWarning)

app = Flask(__name__)
app.config.from_object(ProdConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
