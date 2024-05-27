# создание БД. Соединение и разрыв с ней
import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort
from selfedu.les9.FDataBase import FDataBase

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
    dbase = FDataBase(db)  # для подтягивания меню из таблицы
    return render_template('index.html', menu=dbase.getMenu(), posts=dbase.getPostsAnonce())


# Обрабочик для добавления статьи
@app.route('/add_post/', methods=['POST', 'GET'])
def addPost():
    db = get_db()  # соединяемся с БД
    dbase = FDataBase(db)  # Создаем экземпляр класса dbase
    if request.method == 'POST':  # Если пришли данные после заполнения формы
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:  # Если заголовок более 4 симв, статья более 10 симв
            res = dbase.addPost(request.form['name'], request.form['post'])  # то добавляем пост в БД (заголовок и ствтью)
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')
    return render_template('add_post.html', menu=dbase.getMenu(), title='Добавление статьи')


# обработчик для отображения статьи
@app.route('/post/<int:id_post>/')
def showPost(id_post):
    db = get_db()  # соединяемся с БД
    dbase = FDataBase(db)  # соединяемся с БД
    title, post = dbase.getPost(id_post)  # берем статью из БД
    if not title:  # если статья не получена из БД
        abort(404)
    # post = dbase.getPost(id_post)  # берем статью из БД
    # if not post:  # если статья не получена из БД
    #     abort(404)
    # title, text = post
    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


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
