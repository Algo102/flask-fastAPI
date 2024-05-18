# 400 - неверный запрос
# 401 - не авторизован
# 403 - доступ запрещен
# 404 - страница не найдена
# 500 - ошибка сервера


# Имитируем ошибку сервера

from flask import Flask, request, render_template, abort

# from lessons.lec2.db import get_blog  # Специально убрали импорт


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)
    # возвращаем найденную в БД статью


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


@app.errorhandler(500)
def page_not_found(e):
    app.logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
