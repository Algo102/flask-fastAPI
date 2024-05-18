from flask import Flask, render_template

app = Flask(__name__)


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


@app.route('/jackets/')
def jackets():
    content = {'title': 'Куртки'}
    jacket_items = [
        {
            'text': 'Стеганая куртка - удобный и стильный вариант на каждый день',
            'image': 'jaket_1.jpg'
        },
        {
            'text': 'Куртка для комфортных весенних прогулок. Внутри - утеплитель Downfill',
            'image': 'jaket_2.jpg'
        },
        {
            'text': 'Необычный, но лаконичный дизайн куртки отлично впишется в любой гардероб',
            'image': 'jaket_3.jpg'
        },
    ]
    return render_template('jackets.html', **content, jackets=jacket_items)


@app.route('/costumes/')
def costumes():
    content = {'title': 'Костюмы'}
    return render_template('costumes.html', **content)


if __name__ == '__main__':
    app.run()
