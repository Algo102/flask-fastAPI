from flask import Flask
from flask_wtf.csrf import CSRFProtect
# Защита от перехвата трафика

app = Flask(__name__)
app.config['SECRET_KEY'] = '605314a4fad7f963c94b3b69571e7abee77998f909bcdb1d23b8bd89725dc50a'
csrf = CSRFProtect(app)

# генерация надежного секретного ключа в консоле
# import secrets
# secrets.token_hex()


@app.route('/')
def index():
    return 'Hi!'


# Отключение защиты. Когда передаю что то сам себе и уверены что не будет
# перехвата. При этом повышается скорость передачи
@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protected'


if __name__ == '__main__':
    app.run(debug=True)