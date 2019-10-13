from app import app, db
from app.models import ImageModel
from app.forms import UploadImageForm
from flask import (
    render_template, send_from_directory, abort, url_for,
    request, redirect, jsonify, flash
)
from PIL import Image
from werkzeug.utils import secure_filename


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadImageForm()
    if form.validate_on_submit():
        f = form.image.data
        f_name = secure_filename(f.filename)
        try:
            i = ImageModel(file_name=f_name)
            img_f = Image.open(f)
            i.save_image(img_f)
            i.save_thumbnail(img_f)
            db.session.add(i)
            db.session.commit()
        except (Image.DecompressionBombWarning, Image.DecompressionBombError) as e:
            print(e)
            flash('Decompression bomb error.')
        except AssertionError as e:
            print(e)
            flash(str(e))
        except Exception:
            flash('Something went wrong while saving file')
        return redirect(url_for('index'))
    return render_template('index.html', title='hello', form=form)


@app.route('/api/<string:method>')
def api(method):
    if method == 'get_images':
        imgs = ImageModel.query.all()
        imgs = list(map(
            lambda img: {
                'id': img.id,
                'name': img.file_name,
                'file_url': url_for('media', filename=img.file_path),
                'thumbnail_url': url_for('media', filename=img.thumbnail_path)
            },
            imgs
        ))
        return jsonify({'images': imgs})
    else:
        abort(404)


@app.route('/test')
def test():
    q = ImageModel.query.all()
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
