# pip install email-validator нужно установить, без установки
# ошибку не показывает, только при запуске

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.datetime import DateField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from datetime import datetime


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
    birthdate = DateField('Дата рождения (ДД-ММ-ГГГГ)', format='%Y-%m-%d', validators=[DataRequired(message="Дата рождения обязательна")])
    consent = BooleanField('Согласие на обработку персональных данных', validators=[DataRequired()])

