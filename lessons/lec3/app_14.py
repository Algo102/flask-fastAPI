# pip install flask-wtf для рабдоты с формами

from flask import Flask
from flask_wtf import FlaskForm
# Определение классов форм, описание полей, валидация

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    app.run(debug=True)