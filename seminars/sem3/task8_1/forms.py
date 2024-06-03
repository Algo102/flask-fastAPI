# pip install email-validator нужно установить, без установки
# ошибку не показывает, только при запуске

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    birthdate = StringField('Дата рождения', validators=[DataRequired()])
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6, max=20)])
    password_confirm = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
