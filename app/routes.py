from app import app, db
from app.models import ImageModel
from app.forms import UploadImageForm
from flask import (
    render_template, send_from_directory, abort, url_for,
    request, redirect, jsonify, flash
)
from PIL import Image
from werkzeug.utils import secure_filename
ACCEPTED_EXTENSIONS = {'jpg', 'jpeg', 'bmp', 'png', 'gif'}


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadImageForm()
    if form.validate_on_submit():
        f = form.image.data
        f_name = secure_filename(f.filename)
        try:
            file, extension = f_name.rsplit('.', 1)
            if extension not in ACCEPTED_EXTENSIONS:
                flash('The file should be an image', category='error')
                return redirect(url_for('index'))
            i = ImageModel(file_name=f_name)
            img_f = Image.open(f)
            i.save_image(img_f)
            i.save_thumbnail(img_f)
            db.session.add(i)
            db.session.commit()
        except (Image.DecompressionBombWarning, Image.DecompressionBombError) as e:
            print(e)
            flash('Decompression bomb error.', category='error')
        except AssertionError as e:
            print(e)
            flash(str(e), category='error')
        except Exception:
            flash('Что-то пошло не так, пока мы сохраняли вашу фотографию :(', category='error')
        return redirect(url_for('index'))
    return render_template('index.html', title='Мой альбом', form=form)


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
    elif method == 'delete_image':
        if 'id' in request.args:
            img_id = request.args['id']
        else:
            abort(404)
            return
        img = ImageModel.query.get_or_404(img_id)
        img.delete_image()
        img.delete_thumbnail()
        db.session.delete(img)
        db.session.commit()
        return jsonify({'status': 'ok'})
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
        if 'type' in request.args and request.args['type'] == 'attach':
            return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    else:
        abort(404)
