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


@app.cli.command('add-vaha2')
def add_user():
    user = User(username='vaha2', email='vaha2@gmail.com')
    db.session.add(user)
    db.session.commit()
    print('vaha2 add in DB!')


# при редактировании, нужно закрывать базу
@app.cli.command('edit-john')
def edit_user():
    # С помощью фильтра находим запись, еслиб записей John было больше, искали бы первого
    user = User.query.filter_by(username='John').first()
    user.email = 'new_email@gmail.com'
    db.session.commit()  # Зафиксировали изменения
    print('Edit John mail in DB')


# обычно ничего не удаляют, а добавляют новую колонку со значением False,
# а у всех остальных значение True
@app.cli.command('del-john')
def del_user():
    user = User.query.filter_by(username='John').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John mail in DB')


@app.cli.command('del-smith')
def del_user():
    user = User.query.filter_by(username='Smith').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete Smith mail in DB')


@app.cli.command('del-vaha')
def del_user():
    user = User.query.filter_by(username='Vaha').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete Vaha mail in DB')


@app.cli.command('del-vaha2')
def del_user():
    user = User.query.filter_by(username='vaha2').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete vaha2 mail in DB')


if __name__ == '__main__':
    app.run(debug=True)


