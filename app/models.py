from app import db, app
from config import BASE_DIR
from os import listdir
from os.path import join, normpath, isfile


class ImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(64), unique=True, index=True)
    file_path = db.Column(db.String(128), unique=True, index=True)
    thumbnail_path = db.Column(db.String(128), unique=True, index=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        files = []
        for file in listdir(join(BASE_DIR, normpath('media/images'))):
            if isfile(join(BASE_DIR, normpath('media/images'), file)):
                files.append(file)
        file = self.file_name
        assert file not in files, 'File with this name already exist'
        f_name, f_extension = file.rsplit('.', 1)
        self.file_path = f'images/{file}'
        self.thumbnail_path = f'thumbnails/{file}'

    def save_image(self, image_file):
        image_file.save(join(app.config['UPLOAD_FOLDER'], 'images', self.file_name))

    def save_thumbnail(self, image_file):
        width, height = image_file.size
        side = min(width, height)
        left, upper = (width - side) // 2, (height - side) // 2
        right, lower = left + side, upper + side
        image_file = image_file.crop((left, upper, right, lower))
        image_file.thumbnail((200, 200))
        image_file.save(join(app.config['UPLOAD_FOLDER'], 'thumbnails', self.file_name))

    def __repr__(self):
        return f'<ImageModel file_name="{self.file_name}">'
