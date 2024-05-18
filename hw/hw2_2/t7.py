# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index7.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        number = float(request.form['number'])
        square = number * number
        return render_template('res.html', number=number, square=square)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
