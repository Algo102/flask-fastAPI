from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return f'Привет, {name.capitalize()}!'


@app.route('/file/<path:file>/')  # http://127.0.0.1:5000/file/ssdfsd/sdfsdf/sdfs/
def set_path(file):  # Путь, "ssdfsd/sdfsdf/sdfs"
    print(type(file))
    return f'Путь, "{file}"'


@app.route('/number/<float:num>/')  # http://127.0.0.1:5000/number/42.3/
def set_number(num):
    print(type(num))
    return f'Переданное число, "{num}"'  # Переданное число, "42.3"


if __name__ == '__main__':
    app.run(debug=True)