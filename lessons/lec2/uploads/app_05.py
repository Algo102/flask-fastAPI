# POST запросы используются для отправки данных на сервер от
# клиента обычно с помощью HTML кода
# в GET запросе - адресная строка, которую видно явно
# в POST запросе - набор байт


from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


# декоратор принимает и гет и пост запросы, по умолчанию GET
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # Если метод равен POST
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')  # Срабатывает GET


if __name__ == '__main__':
    app.run(debug=True)