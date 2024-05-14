from flask import Flask, render_template

app = Flask(__name__)

# <name> - переменные в маршрутах
# {{name}} - переменные в шаблонах, если в html нет этой переменно, то проблем не будет


@app.route('/')
def index():
    return 'Hi!'


@app.route('/index/')
def html_index():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон',
    }
    return render_template('index2.html', **context)
# **context - распаковывает переменную на ключ и значение


if __name__ == '__main__':
    app.run(debug=True)
