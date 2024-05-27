from flask import Flask
from lessons.lec3.models_05 import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


# модуль cli для запуска команд с консоли
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


# add-john команда для консоли
# т.к. wsgi не в корне, то
# flask --app lessons.lec3.app_06 add-john
@app.cli.command('add-john')
def add_user():
    user = User(username='John', email='john@gmail.com')
    db.session.add(user)  # Пользователь появился но фиксации еще нет
    db.session.commit()  # Добавляем пользователя в базу даннных
    print('John add in DB!')


@app.cli.command('add-smith')
def add_user():
    user = User(username='Smith', email='smith@gmail.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


@app.cli.command('add-vaha')
def add_user():
    user = User(username='Vaha', email='vaha@gmail.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


if __name__ == '__main__':
    app.run(debug=True)
