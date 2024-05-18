from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.secret_key = b'e236e8d5008cf89ac35084b84f6389a248c7062b4c62c50bf2b6aa5eb6474b26'

# Генерация секретного надежного ключа в Python Console
# import secrets
# secrets.token_hex()


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)