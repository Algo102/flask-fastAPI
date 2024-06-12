# Проверка параметра пути через Path. fastapi. Path — это класс
#
# Пример 1:
from fastapi import FastAPI, Path, Query

app = FastAPI()


# Используем Path т.к. id  это часть строки, а не пара ключ-значение
# @app.get("/items/{item_id}")
# async def read_item(item_id: int = Path(..., ge=1)):
#     return {"item_id": item_id}


# Пример 2:
# @app.get("/items/{item_id}")
# async def read_item(item_id: int = Path(..., title="The ID of the item", ge=1), q: str = None):
#     return {"item_id": item_id, "q": q}
# # int - обязательное значени, а q - нет


# Проверка параметра запроса через Query. fastapi.Query — это класс

# Пример 1:


@app.get("/items/")
# async def read_items(q: str = Query(None, min_length=3, max_length=50)):
async def read_items(q: str = Query(..., min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q:
        results.update({"q": q})
    return results
