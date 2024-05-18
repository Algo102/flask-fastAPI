# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# 📌 При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.
from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        word_count = len(re.findall(r'\w+', text))
        return redirect(url_for('result', word_count=word_count))

    return render_template('index4.html')


@app.route('/result/<int:word_count>')
def result(word_count):
    return render_template('result.html', word_count=word_count)


if __name__ == '__main__':
    app.run(debug=True)
