from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FIleField, FIleRequired, FileAllowed
from wtforms import TextAreaField
from wtform.validators import DataRequired

class UploadForm(FlaskForm):
    description = StringField ('Description', validators=[DataRequired()])
    photo = FIleFiled('Upload Photo', validators=[FileREquired(),FileAllowed(['jpg','jpeg','png', 'Images only'])])