from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, незнакомец!'


# Написав второй / - гарантируем запуск, т.к. браузер сам допишет, а если
# ее не будет, а пользоваель напишет, то будет ошибка
@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'


@app.route('/Иван/')
def ivan():
    return 'Привет, Ванюша!'


@app.route('/Фёдр/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Федя!'


if __name__ == '__main__':
    app.run(debug=True)