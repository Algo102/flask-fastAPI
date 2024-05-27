from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


# Создали дочерний класс, который наследуется от базового FlaskForm
class LoginForm(FlaskForm):
    # Импортируем два поля, с обязательным заполнением
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# Поля форм
# StringField
# IntegerField
# FloatField
# BooleanField - чекбокс
# SelectField - выпадающий список
# DataField - ввод даты
# FileField - загрузка файла
# PasswordField
