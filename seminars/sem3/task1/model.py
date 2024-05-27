from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    group = db.Column(db.Integer)
    gender = db.Column(db.String(5))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'User({self.firstname}, {self.lastname})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty({self.name}'
