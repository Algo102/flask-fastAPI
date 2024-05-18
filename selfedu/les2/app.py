from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# menu = ['Установка', 'Первое приложение', 'Обратная связь']
menu = [{'name': 'Установка', 'url': 'install-flask'},
        {'name': 'Первое приложение', 'url': 'first-app'},
        {'name': 'Обратная связь', 'url': 'contact'}]


@app.route('/index/')
@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about/')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        print(request.form)  # Выводим в терминал все данные
        print(request.form['username'])  # Выводим в терминал только юзера
        # таким образом на сервере можно забирать данные от клиента
    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.route('/profile/<path:username>')  # http://127.0.0.1:5000/profile/avafv/daf
def profile_p(username):
    return f'Пользователь {username}'


@app.route('/profile/<int:username>')  # http://127.0.0.1:5000/profile/13
def profile_i(username):
    return f'Пользователь {username}'


@app.route('/profile/<int:username>/<path>')  # http://127.0.0.1:5000/profile/13/sdfg
def profile_i_p(username, path):
    return f'Пользователь {username}, {path}'


@app.route('/profile/<username>')
def profile(username):
    return f'Пользователь {username}'


# # для вывода теста в терминал, без запуска сервера
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username='alex'))


if __name__ == '__main__':
    app.run(debug=True)
