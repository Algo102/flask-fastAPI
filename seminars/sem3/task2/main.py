from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from task2.model import db, Book, Author, BookAuthor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


@app.cli.command('init_db')
def init_db():
    with app.app_context():
        db.create_all()
        print('OK')

# в терминале пишем flask init_db, чтоб создалась БД и instance
# при условии что в терминале находимся в папке sem3


# @app.cli.command('fill-db')
# def fill_dables():  # Добавляем студентов в факультеты
#     count = 5
#     for i in range(1, count + 1):
#         faculty = Faculty(name=f'faculty{i}')
#         db.session.add(faculty)
#         for j in range(1, count + 1):
#             student = Student(firstname=f'student{i}_{j}', lastname=f'student_{i}_{j}',
#                               age=18, gender='male', group='math', faculty_id=i)
#             db.session.add(student)
#     db.session.commit()


@app.route('/books/')
def books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)


if __name__ == '__main__':
    pass
