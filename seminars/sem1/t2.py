# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# 📌 Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# 📌 Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)

_users = [{'name': 'Никанор',
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

@app.route('/table/')
def table():

    return render_template('table.html', users=_users)


if __name__ == '__main__':
    app.run()
