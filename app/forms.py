from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class UploadImageForm(FlaskForm):
    image = FileField('Картинка', validators=[FileRequired()])
    submit = SubmitField('Загрузить картинку')
