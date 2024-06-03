from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
# generate_password_hash - зашифровывает пароль
# check_password_hash - сравнивает с зашифрованным паролем в базе
from task8.forms import RegisterForm

from task8.model import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_hw8.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'asvafvsdgbfgnhnf3453bcb4'
csrf = CSRFProtect(app)


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')

# в терминале пишем flask init_db, чтоб создалась БД и instance
# при условии что в терминале находимся в папке sem3


@app.route("/registration/", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    context = {"title": "Страница регистрации", "form": form}
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        mail = form.mail.data

        secret_password = generate_password_hash(form.password.data)

        user = User.query.filter_by(mail=mail).first()
        if user:
            flash(
                "Пользователь с такой электронной почтой уже зарегистрирован!", "danger"
            )
            return redirect(url_for("registration"))

        new_user = User(name=name, surname=surname, mail=mail, password=secret_password)
        db.session.add(new_user)
        db.session.commit()

        flash(f"Здравствуйте {name} {surname}!Вы зарегистрированы!!!", "success")
        return redirect(url_for("index"))
    return render_template("registration.html", **context)


if __name__ == '__main__':
    pass
