# .\venv\Scripts\Activate.ps1
# pip install fastapi
# Если во Flask сервер стоит по умолчанию, то в FastAPI ставим его отдельно
# pip install 'uvicorn[standard]'
# Для запуска приложения
# uvicorn lessons.les5_fastAPI.main_01:app --reload
# Также эту строку можно прописать в пайчарм, чтоб запускать по кнопке

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/items/{item_id}')  # в {} переменная
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
# в браузере можем написать http://127.0.0.1:8000/items/42?q=qwe
# получаем {"item_id":42,"q":"qwe"}

# Обработка HTTP-запросов и ответов
# GET - получение ресурсов с сервера
# POST -  отправка данных на сервер
# PUT - обновление данных на сервере
# DELETE -  удаление данных на сервере
