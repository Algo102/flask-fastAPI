# Загрузка файлов от клиента, сохраняем на сервере через POST запрос
from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
# secure_filename - для получения безопасного имени

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


if __name__ == '__main__':
    app.run()