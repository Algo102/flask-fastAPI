from flask import Flask
from lessons.lec3.models_05 import db, User, Post


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


@app.cli.command('fill-db')
def fill_dables():
    count = 5
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()

    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'post title {post}', content=f'post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()


# add-john команда для консоли
@app.cli.command('add-john')
def add_user():
    user = User(username='John', email='john@gmail.com')
    db.session.add(user)  # Пользователь появился, но фиксации еще нет
    db.session.commit()  # Добавляем пользователя в базу даннных
    print('John add in DB!')


@app.cli.command('edit-john')
def edit_user():
    # С помощью фильтра находим запи
    user = User.query.filter_by(username='John').first()
    user.mail = 'newjohn-email.gmail.com'
    db.session.commit()  # Зафиксировали изменения
    print('Edit john mail in DB')


@app.cli.command('del-john')
def del_user():
    user = User.query.filter_by(username='John').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John mail in DB')


if __name__ == '__main__':
    app.run(debug=True)


