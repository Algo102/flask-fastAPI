# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# 📌 Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# 📌 Данные о новостях должны быть переданы в шаблон через контекст.
from flask import Flask, render_template

app = Flask(__name__)

_news = [{'title': 'Никанор',
          'content': 'lorem ipsum dolor sit',
          'date': '2024-02-04',
          },
         {'title': 'Феофан',
          'content': 'lorem5 ipsum dolor sit',
          'date': '2024-03-03',
          },
         {'title': 'Оверран',
          'content': 'lorem6 ipsum dolor sit',
          'date': '2024-05-05',
          }, ]


@app.route('/news/')
def news():
    return render_template('news.html', news=_news)


if __name__ == '__main__':
    app.run()
