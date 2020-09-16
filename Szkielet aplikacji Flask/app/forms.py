from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    name = StringField('Imię i nazwisko', validators=[InputRequired()])
    email = StringField('Adres e-mail', validators=[InputRequired()])
