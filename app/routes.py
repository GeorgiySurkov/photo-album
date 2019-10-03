from app import app, db
from app.models import Image
from flask import (
    render_template, send_from_directory, abort, url_for
)


@app.route('/')
def index():
    return render_template('index.html', title='hello')


@app.route('/test')
def test():
    q = Image.query.all()
    i = q[0]
    return f'<img src="{url_for("media", filename=str(i.file_path))}", alt="котик">'


@app.route('/media/<path:filename>')
def media(filename):
    accepted_dirs = (
        'images',
        'thumbnails'
    )
    if filename.split('/')[0] in accepted_dirs:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    else:
        abort(404)
