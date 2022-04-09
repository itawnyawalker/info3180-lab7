from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description = TextAreaField ('Description', validators=[DataRequired()])
    photo = FileField('Upload Photo', validators=[FileRequired(),FileAllowed(['jpg','jpeg','png', 'Images only'])])