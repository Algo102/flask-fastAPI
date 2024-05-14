from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Инициируем приложение фласк
# sqlite - приложение из коробки
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

# Базы данных ниже нужно устанавливать дополнительно
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/db_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycorg2://username:password@hostname/db_name'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)