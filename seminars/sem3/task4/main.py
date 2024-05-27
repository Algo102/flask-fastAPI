from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from task4.forms import RegisterForm

from flask_sqlalchemy import SQLAlchemy
from task4.model import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'asvafvsdgbfgnhnf3453bcb4'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hello'


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')

# в терминале пишем flask init_db, чтоб создалась БД и instance
# при условии что в терминале находимся в папке sem3


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из форм
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print(name, email, password)
        return "Данные введены верно, Вы зарегистрированы"
    else:
        return render_template('registration.html', form=form)


if __name__ == '__main__':
    pass
