# создание БД. Соединение и разрыв с ней
import sqlite3
import os
from flask import Flask, render_template, request, redirect, g

# переменные для начальной конфигурации
DATABASE = '/tmp/flsite.db'  # Путь к БД
DEBUG = True  # Режим отладки включен
SECRET_KEY = 'vfvsdvd86ds7fvdsf64dsfvnb'

app = Flask(__name__)  # - создаем приложение
app.config.from_object(__name__)
# from_object - из какого модуля загружать конфигурацию(__name__ - из текущего)

# переопределяем путь к БД. root_path - ссылается на текущий каталог
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


# функция для установлния соединения с БД
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row  # Чтоб записи были представлены ввиде словаря, а не кортежей
    return conn


# функция создает БД(с набором таблиц) без запуска веб сервера
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        sql_script = f.read()
        print(sql_script)  # Выводим содержимое скрипта для отладки
        db.cursor().executescript(sql_script)  # executescript запускает скрипты из sq_db.sql
    db.commit()  # записываем изменения
    db.close()  # закрываем соединение


# соединение с БД, если еще не установлено
def get_db():
    if not hasattr(g, 'link_db'):  # усли у g есть свойство link_db
        g.link_db = connect_db()  # если нет то вызываем функцию
    return g.link_db


@app.route('/')
def index():
    db = get_db()
    return render_template('index.html', menu=[])


# разорвать соединение, если оно ранее было установлено
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


# в консоле без запуска на сервере, запускаем функцию
# from selfedu.les8.flsite import create_db
# create_db()


if __name__ == '__main__':
    app.run(debug=True)
