from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from task3.model import Gender, db, Student, Faculty, Evaluation
from random import choice, randint

# Добавляем и заполняем БД
# flask init_db
# flask fill_db

# Запуск flask run


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_hw3.db'
db.init_app(app)

COUNT = 10


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data/')
def data():
    return 'Интересная информация для Вас'


@app.route('/students/')
def students():
    students = db.session.query(Student).all()
    student_evaluations = db.session.query(Evaluation).all()
    return render_template('students.html', student=students, evaluations=student_evaluations)


@app.cli.command('init_db')
def initdb_command():
    db.create_all()
    print('Initialized the database.')


@app.cli.command('fill_db')
def fill_db():
    for student in range(1, COUNT + 1):
        new_student = Student(
            name=f'student{student}',
            last_name=f'last_name{student}',
            age=choice([student, student * 5]),
            gender=choice([Gender.male, Gender.female]),
            group=f'group{student}', faculty_id=randint(1, 10, ),
            email=f'student{student}@example.com'
        )
        db.session.add(new_student)
    db.session.commit()

    for faculty in range(1, COUNT + 1):
        new_faculty = Faculty(faculty_name=f'faculty{faculty}')
        db.session.add(new_faculty)
    db.session.commit()


@app.cli.command('fill_evaluations')
def fill_evaluations():
    for student in range(1, COUNT + 1):
        for evaluation in range(1, 4):
            new_evaluation = Evaluation(
                title=f'Academic_discipline{evaluation}',
                value=randint(1, 5),
                student_id=Student.query.get(student).id_,
            )
            db.session.add(new_evaluation)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
