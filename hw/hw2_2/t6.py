# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index6.html')


@app.route('/check_age', methods=['POST'])
def check_age():
    name = request.form['name']
    age = int(request.form['age'])

    if age >= 18:
        return redirect(url_for('result', name=name, age=age))
    else:
        return redirect(url_for('error'))


@app.route('/result')
def result():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'Привет, {name}! Тебе уже есть {age} лет, добро пожаловать!'


@app.route('/error')
def error():
    return f'Тебе еще рано, приходи когда будет 18'


if __name__ == '__main__':
    app.run(debug=True)
