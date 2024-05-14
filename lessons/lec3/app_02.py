from flask import Flask
from lessons.lec3.models_02 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# Строка инициализации. Импортировали db из models_02. Вызвали метод
# init_app, и предали в него объект нашего приложения
db.init_app(app)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)