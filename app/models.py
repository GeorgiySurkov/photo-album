from app import db, app
from config import BASE_DIR
from os.path import join as path_join, normpath


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(64), unique=True, index=True)
    file_path = db.Column(db.String(96), unique=True, index=True)

    def set_file_path(self):
        # TODO check for files with the same names

        # files = []
        # for dir_entry in os.scandir()
        file_name = self.file_name
        # file_extension = file_name.rsplit('.', 1)[-1]
        self.file_path = path_join(app.config['UPLOAD_FOLDER'], normpath(f'images/{file_name}'))

    def __repr__(self):
        return f'<Image file_name="{self.file_name}">'
