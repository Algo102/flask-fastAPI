# Генерация URL адресов

from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) = }<br>'
    return text
# в url_for передали функцию test_url


if __name__ == '__main__':
    app.run(debug=True)

# В num лежит 123
# Функция url_for("test_url", num=42) = '/test_url_for/42/'
# Функция url_for("test_url", num=42, data="new_data") = '/test_url_for/42/?data=new_data'
# Функция url_for("test_url", num=42, data="new_data", pi=3.14515) = '/test_url_for/42/?data=new_data&pi=3.14515'
# ? - перед парой ключ-значение, разделенные =
# & - между парами
# test_url_for - обязательная строка
# url_for - сохраняет обязательную строку
