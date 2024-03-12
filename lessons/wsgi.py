from lec1.app_01 import app

# Запускаем программу с этого файла, в режиме отладки
if __name__ == '__main__':
    app.run(debug=True)


# находясь в терминале, там же где и файл wsgi.py,
# программу можно запустить написав flask run