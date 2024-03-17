# Для перенаправления в Flask используется функция redirect().
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


# при попытки перейти на redirect, переходит к фунции index на
# главную страницу при помощи url_for
@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


# С помощью redirect перенаправили на внешний URL
@app.route('/external')
def external_redirect():
    return redirect('https://www.python.org/')


@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'


# в адресной строке будет http://127.0.0.1:5000/hello/Alex,
# т.к. пренаправили на функцию hello
@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()