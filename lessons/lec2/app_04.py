# Обработка GET запросов. Адресная строка, и запрос виден явно
from flask import Flask, request
# request для доступа к значениям, которые передаются от клиента к серверу


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'

# http://127.0.0.1:5000/get/?name=alex&age=13&level=80
@app.route('/get/')
def get():
# request получает доступ к объекту кортеж, а именно к неизменяемому словарю
# get возвращает значение ключа если есть, если нет то 0
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level} <br> '
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'


if __name__ == '__main__':
    app.run(debug=True)
