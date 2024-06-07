# Создание конечных точек
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {"Hello": "World"}


# Работа с параметрами запроса и путями URL
# http://127.0.0.1:8000/items/4?q=999  ---  {"item_id":4,"q":"999"}
@app.get('/items/{item_id}')
async def update_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {'item_id': item_id}


# http://127.0.0.1:8000/users/4/orders/555  ---  {"user_id":4,"oreder_id":555}
@app.get('/users/{user_id}/orders/{oreder_id}')
async def read_data(user_id: int, oreder_id: int):
    # обработка данных
    return {"user_id": user_id, "oreder_id": oreder_id}


# Не будет ошибки, если ничего не передадим, т.к. есть значения по умолчанию
# http://127.0.0.1:8000/items/?limit=25  ---  {"skip":0,"limit":25}
# http://127.0.0.1:8000/items/?limit=25&skip=10 ---  {"skip":10,"limit":25}
@app.get("/items/")  # {"skip":0,"limit":10}
async def skip_limit(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
