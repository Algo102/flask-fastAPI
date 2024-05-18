# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".
from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = '83eb72a18e3345db3e914f4dff68c0378052a32f7e82c5368628fea7e414ad3d'

# Генерация секретного надежного ключа
# import secrets
# secrets.token_hex()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        flash(f'Привет, {name}!')
        return redirect(url_for('message'))
    return render_template('index8.html')


@app.route('/message')
def message():
    return render_template('message.html')


if __name__ == '__main__':
    app.run(debug=True)
