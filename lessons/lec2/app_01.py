# Экранирование

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def index():
    return 'Введите путь к файлу в адресной строке'


@app.route('/<path:file>/')
def serve_file(file):
    print(file)
    # return f'Ваш файл находится в :{file}'  # Так делать нельзя, т.к. код виден всем
# могут работать скрипты злоумышлеников, например
# http://127.0.0.1:5000/%3Cscript%3Ealert(%22I%20am%20ha%D1%81ker%22)%3C/script%3E/
    return f'Ваш файл находится в :{escape(file)}'  # запуск с экранированием, скрипт не сработает
    # escape - говорит что будем работать только с текстом, интерпритировать не нужно
    # при получении данных от пользователя их нужно экранировать

if __name__ == '__main__':
    app.run(debug=True)