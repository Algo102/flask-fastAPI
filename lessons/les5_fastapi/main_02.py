# .\venv\Scripts\Activate.ps1
# pip install fastapi
# Если во Flask сервер стоит по умолчанию, то в FastAPI ставим его отдельно
# pip install 'uvicorn[standard]'
# Для запуска приложения
# uvicorn lessons.les5_fastAPI.main_01:app --reload


from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get('/')
async def root():
    logger.info('Отработал GET запрос')
    return {"Hello": "World"}


@app.get('/items/{item_id}')  # в {} переменная
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
# в браузере можем написать http://127.0.0.1:8000/items/42?q=qwe
# получаем {"item_id":42,"q":"qwe"}

# так как отправить некуда, а изменить и удалить нечего, то все закомменитровал
# @app.post('/items/')
# async def create_item(item: Item):
#     logger.info('Отработан POST запрос')
#     return item


# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item):
#     logger.info(f'Отработан PUT запрос для item_id = {item_id}.')
#     return {'item_id': item_id, 'item': item}


# @app.delete('/items/{item_id}')
# async def delete_item(item_id: int):
#     logger.info(f'Отработан DELETE запрос для item_id = {item_id}.')
#     return {'item_id': item_id}
# Но лучше не удалять запись, а ставить пометку в доп. поле False или Delete


# Обработка HTTP-запросов и ответов
# GET - получение ресурсов с сервера
# POST - отправка данных на сервер
# PUT - обновление данных на сервере
# DELETE - удаление данных на сервере
