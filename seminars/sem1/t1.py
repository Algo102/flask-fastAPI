# 1. Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".
# 2. Добавьте две дополнительные страницы в ваше веб-приложение:
# ○ страницу "about"
# ○ страницу "contact".
# 3. Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.
# 4. Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.
# 5. Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'About'


@app.route('/contact/')
def contact():
    return 'Contact'


@app.route('/summ/<int:num1>/<int:num2>/')  # можно сразу переменные передать без summ
def summation(num1, num2):
    return str(num1 + num2)


@app.route('/lenstr/<text>/')  # string: указывать не обязательно(по умолчанию)
def lenstr(text):
    return str(len(text))


@app.route('/get-lenght/<string:row>')
def get_lenght(row):
    return str(len(row))


html = """
<h1>Моя первая страница</h1>
<p> Привет мир!</p>
"""


@app.route('/web/')
def webpage():
    # return html
    # или
    return """
            <h1>Моя первая страница</h1>
            <p> Привет мир!</p>
            """


if __name__ == '__main__':
    app.run()
