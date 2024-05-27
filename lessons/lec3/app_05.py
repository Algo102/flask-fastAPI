from flask import Flask
from lessons.lec3.models_05 import db, User, Post, Comment
# Обязательно нужно импортировать все модели, даже если их не используем

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello World!'


@app.cli.command('init-db')
def init_db():
    # показать ошибку с неверным wsgi.py
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)

# в терминале запускаем при условии, что wsgi корректен
# flask init-db
# т.к. wsgi не в корне, то
# flask --app lessons.lec3.app_05 init-db
# в папке instance появилась БД
