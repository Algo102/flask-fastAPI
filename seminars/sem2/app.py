import fileinput
from pathlib import PurePath, Path

from flask import Flask, render_template, request, redirect, url_for, abort, flash, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = b'e236e8d5008cf89ac35084b84f7389a248c7062b4c62c50bf2b6aa5eb6474b26'
# app.config['SECRET_KEY'] = b'dasfsagdfsvssgbfgfgfghghsgewrgxcvx'

# Генерация секретного надежного ключа в Python Console
# import secrets
# secrets.token_hex()

# # а можно и в app написать
# import secrets
# app.secret_key = secrets.token_hex()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello():
    return f'Hello friend!'


@app.route('/upload_img/', methods=['GET', 'POST'])
def upload_img():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'File {file_name} uploaded!'
    return render_template('upload.html')


@app.route('/log_in/', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == 'login' and password == 'password':
            return f'Wellcome {login}! Please'
        return f'Invalid login, password!'
    return render_template('log_in.html')


@app.route('/check_txt/', methods=['GET', 'POST'])
def check_txt():
    if request.method == 'POST':
        txt = request.form.get('text')
        return f'Lenght: {len(txt)}'
    return render_template('check_txt.html')


@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form.get('a'))
        num2 = int(request.form.get('b'))
        oper = request.form.get('operation')
        if oper == 'add':
            return f'{num1} + {num2} = {num1 + num2}'
        elif oper == 'substract':
            return f'{num1} - {num2} = {num1 - num2}'
        elif oper == 'multiplay':
            return f'{num1} * {num2} = {num1 * num2}'
        elif oper == 'divide':
            return f'{num1} / {num2} = {num1 / num2}'
    return render_template('calc.html')


@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age >= 18:
            return f'Welcome {name}'
        else:
            abort(403)
    return render_template('check_age.html')


@app.errorhandler(403)
def forbidder_err(e):
    app.logger.warning(e)
    print(e)
    context = {
        'title': 'Доступ запрещен',
        'url': request.base_url,
    }
    return render_template('403.html', **context), 403


@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        num = int(request.form.get('a'))
        return redirect(url_for('square_res', num=num))  # через redirect на функцию
        # return f'{num} в квадрате = {num * num}'
    return render_template('square.html')


@app.route('/square_res/<int:num>')
def square_res(num):
    return f'{num} в квадрате = {num ** 2}'


@app.route('/greetings/', methods=['GET', 'POST'])
def greetings():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'{name}, все успешно отправлено!', 'success')
        return redirect(url_for('greetings'))
    return render_template('welcome.html')


@app.route('/form_mail/', methods=['GET', 'POST'])
def form_mail():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        flash(f'{name}, Вы успешно вошли', 'success')
        response = make_response(render_template('welcome_log.html', name=name))
        response.set_cookie('user_data', f'name={name}&email={email}')
        return response
    return render_template('form_mail.html')


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('user_data', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
