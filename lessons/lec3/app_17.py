from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from forms_3 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '605314a4fad7f963c94b3b69571e7abee77998f909bcdb1d23b8bd89725dc50a'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
    # обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из форм
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)