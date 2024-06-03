from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from model import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


# 0 create_all - в реальной жизни не используют, т.к. при
# добавлении столбца нужно удалять все и создавать новую таблицу
# 1 используют pip install alembic
# 2 в терминале находясь в папке с model пишем alembic init migrations
# создается папка с содержимым и файл alembic
# 3 в файле alembic.ini нужно изменить путь к БД
# sqlalchemy.url = sqlite:///mydatabase.db
# 4 в файле env в папке migrations добавляем импорт и строчку с методатой
# from model import db
# target_metadata = db.Model.metadata
# 5 Создаем структуру миграции, через терминал
# alembic revision --autogenerate -m "initial migration"
# 6 применяем миграцию в терминале, накатываются таблицы
# alembic upgrade head
# 7 Предположим в model факультеты добавили новую колонку decan
# 8 alembic revision --autogenerate -m "add column decan"
# 9 alembic upgrade head


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
