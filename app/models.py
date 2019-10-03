from app import db, app
from config import BASE_DIR
from os.path import join as path_join, normpath


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(64), unique=True, index=True)
    file_path = db.Column(db.String(128), unique=True, index=True)
    thumbnail_path = db.Column(db.String(128), unique=True, index=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO check for files with the same names
        # files = []
        # for dir_entry in os.scandir()
        file = self.file_name
        f_name, f_extension = file.rsplit('.', 1)
        self.file_path = path_join(app.config['UPLOAD_FOLDER'], normpath(f'images/{file}'))
        self.thumbnail_path = path_join(app.config['UPLOAD_FOLDER'], normpath(f'thumbnails/{file}'))

    def __repr__(self):
        return f'<Image file_name="{self.file_name}">'
