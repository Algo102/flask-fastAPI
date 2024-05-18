# Загрузка файлов от клиента, сохраняем на сервере через POST запрос
from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
# secure_filename - для получения безопасного имени (удаляет из
# названия файла разлиичные символы)

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')  # Получаем файл из оперативки или из временных файлов
        file_name = secure_filename(file.filename)  # Удаляем лишние символы
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))  # Сохраняем файл на сервер
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


if __name__ == '__main__':
    app.run()
