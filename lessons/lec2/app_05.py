# POST запросы используются для отправки данных на сервер от клиента
# обычно с помощью HTML кода

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'

# декоратор принимает и гет и пост запросы
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # Если метод равен POST
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)