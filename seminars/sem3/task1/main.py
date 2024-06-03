from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from task1 import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')

# в терминале пишем flask init_db, чтоб создалась БД и instance
# при условии что в терминале находимся в папке sem3


@app.cli.command('fill-db')
def fill_dables():  # Добавляем студентов в факультеты
    count = 5
    for i in range(1, count + 1):
        faculty = Faculty(name=f'faculty{i}')
        db.session.add(faculty)
        for j in range(1, count + 1):
            student = Student(firstname=f'student{i}_{j}', lastname=f'student_{i}_{j}',
                              age=18, gender='male', group='math', faculty_id=i)
            db.session.add(student)
    db.session.commit()


@app.route('/students/')
def students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    pass
