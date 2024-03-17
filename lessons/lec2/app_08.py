# Обработка ошибок 404 декоратором errorhandler.

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


@app.errorhandler(404)
# Функция сработает если пользователь введет несущестыующую страницу
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
# base_url для хранения адреса, который ввел пользователь в командной строке
    }
    return render_template('404.html', **context), 404



if __name__ == '__main__':
    app.run()