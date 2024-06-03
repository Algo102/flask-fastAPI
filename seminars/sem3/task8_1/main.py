from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from task8_1.forms import RegisterForm

from flask_sqlalchemy import SQLAlchemy
from task8_1.model import db, User

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
        username = form.username.data
        email = form.email.data
        password = form.password.data
        birthdate = form.birthdate.data
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            error_msg = 'Username or email already exists'
            form.username.errors.append(error_msg)
            return render_template('registration.html', form=form)

        new_user = User(name=username, email=email, password=password, birthdate=birthdate)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        print(username, email, password)
        return "Данные введены верно, Вы зарегистрированы"
    else:
        return render_template('registration.html', form=form)


if __name__ == '__main__':
    pass
