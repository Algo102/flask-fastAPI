from flask import (Flask, render_template, url_for, request,
                   flash, session, redirect, abort)

app = Flask(__name__)

# app.secret_key = b'307999fb0b36c9e250bc21596985048b7ea1973474b22413b8ea0e3fdfc46be1'
app.config['SECRET_KEY'] = b'dasfsagdfsvssgbfgfgfghghsgewrgxcvx'

# Генерация секретного надежного ключа в Python Console
# import secrets
# secrets.token_hex()


# menu = ['Установка', 'Первое приложение', 'Обратная связь']
menu = [{'name': 'Главная', 'url': '/'},
        {'name': 'Установка', 'url': 'install-flask'},
        {'name': 'Первое приложение', 'url': 'first-app'},
        {'name': 'Обратная связь', 'url': 'contact'},
        {'name': 'Вход', 'url': 'login'},]


# @app.route('/index')
@app.route('/')
def index():
    # print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about/')
def about():
    # print(url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)


@app.route('/contact/', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        # print(request.form)  # Выводим в терминал все данные
        # print(request.form['username'])  # Выводим в терминал только юзера
        # таким образом на сервере можно забирать данные от клиента
        if len(request.form['username']) > 2:  # Если сообщение больше 2-ч символов
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.route('/profile/<username>')
def profile(username):
# Если пользователь захочет в адресной строке указать не свой логин или изночально не будет авторизован
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'Профиль пользователя: <b>{username}</b>'


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'alex' and request.form['password'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu), 404
# 404 в конце можно не писать, тогда в терминале бодет код 200


# @app.route('/profile/<path:username>')  # http://127.0.0.1:5000/profile/avafv/daf
# def profile_p(username):
#     return f'Пользователь {username}'
#
#
# @app.route('/profile/<int:username>')  # http://127.0.0.1:5000/profile/13
# def profile_i(username):
#     return f'Пользователь {username}'
#
#
# @app.route('/profile/<int:username>/<path>')  # http://127.0.0.1:5000/profile/13/sdfg
# def profile_i_p(username, path):
#     return f'Пользователь {username}, {path}'
#
#
# @app.route('/profile/<username>')
# def profile(username):
#     return f'Пользователь {username}'


# # для вывода теста в терминал, без запуска сервера
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username='alex'))


if __name__ == '__main__':
    app.run(debug=True)
