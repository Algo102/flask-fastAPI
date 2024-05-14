# Создание виртуального окружение в папке проекта
python -m venv venv

# Установка flask
pip install flask

# Запуск из коммандной строки или терминала
flask --app .\lessons\lec1\app_01.py run

# находясь в терминале, там же где и файл wsgi.py,
# программу можно запустить написав 
flask run

# с режимом отладки
flask run --debug
