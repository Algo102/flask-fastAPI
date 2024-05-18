from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def index():
#     content = {'title': 'Главная'}
#     return render_template('main.html', **content)

@app.route('/')
@app.route('/main/')
def main():
    content = {'title': 'Главная'}
    return render_template('main.html', **content)


@app.route('/clothes/')
def clothes():
    content = {'title': 'Одежда'}
    return render_template('clothes.html', **content)


@app.route('/shoes/')
def shoes():
    content = {'title': 'Обувь'}
    return render_template('shoes.html', **content)


@app.route('/jacket/')
def jacket():
    content = {'title': 'Куртки'}
    return render_template('jacket.html', **content)


@app.route('/costumes/')
def costumes():
    content = {'title': 'Костюмы'}
    return render_template('costumes.html', **content)


if __name__ == '__main__':
    app.run()
