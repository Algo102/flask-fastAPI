# pip install email-validator нужно установить, без установки
# ошибку не показывает, только при запуске

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
