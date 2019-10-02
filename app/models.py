from app import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(64), unique=True, index=True)
    file_path = db.Column(db.String(96), unique=True, index=True)
