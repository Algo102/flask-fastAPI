from flask import Flask
from lessons.lec3.models_05 import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


# init-db команда для консоли c помощью cli
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


# add-john команда для консоли
@app.cli.command('add-john')
def add_user():
    user = User(username='John', email='john@gmail.com')
    db.session.add(user)  # Пользователь появился, но фиксации еще нет
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


@app.cli.command('edit-john')
def edit_user():
    # С помощью фильтра находим запи
    user = User.query.filter_by(username='John').first()
    user.mail = 'new-email.gmail.com'
    db.session.commit()  # Зафиксировали изменения
    print('Edit John mail in DB')


if __name__ == '__main__':
    app.run(debug=True)


