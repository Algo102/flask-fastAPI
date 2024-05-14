from flask import Flask, render_template

app = Flask(__name__)

_students = [{'name': 'Никанор',
             'lastname': 'Guff',
             'age': '18',
             'average_mark': '4.6',
             },
            {'name': 'Феофан',
             'lastname': 'Smith',
             'age': '25',
             'average_mark': '4.8',
             },
            {'name': 'Оверран',
             'lastname': 'Forest',
             'age': '22',
             'average_mark': '4.7',
             }, ]


@app.route('/students/')
def students():
    return render_template('students.html', students=_students)


_news = [{'title': 'Никанор',
         'content': 'lorem ipsum dolor sit ipsum dolor sit',
         'date': '2024-02-04',
         },
        {'title': 'Феофан',
         'content': 'lorem5 ipsum dolor sit ipsum dolor',
         'date': '2024-03-03',
         },
        {'title': 'Оверран',
         'content': 'lorem10 ipsum dolor sit ipsum dolor orem5 ipsum dolor sit',
         'date': '2024-05-05',
         }, ]


@app.route('/news/')
def news():
    return render_template('news2.html', news=_news)


if __name__ == '__main__':
    app.run(debug=True)
