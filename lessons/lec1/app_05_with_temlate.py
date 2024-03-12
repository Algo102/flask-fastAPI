from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/index/')
def html_index():
    return render_template('index1.html')  # Обязательно помещаем html в папку templates


if __name__ == '__main__':
    app.run(debug=True)