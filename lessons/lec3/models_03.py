# Чтоб работать с таблицами, создаем модель
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'User({self.username}, {self.email})'

# # типы данных для SQLAlchemy
# Integer
# String
# Text - текстовое поле
# Boolean
# DateTime
# Float
# Decimal - десятичное число, более точно чем Float, подходит для денег
# Enum -  перечисление значений
# ForeignKey - внешний ключ к другой таблице
