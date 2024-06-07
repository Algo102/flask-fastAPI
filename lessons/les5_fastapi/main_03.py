# Валидация данных
# pip install fastapi uvicorn pydantic
from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# Создали класс который наследуется от BaseModel из pydantic
class Item(BaseModel):
    name: str  # Обязательные данные
    description: Optional[str] = None  # Если ничего не передать будет None
    price: float
    tax: Optional[float] = None


@app.get('/')
async def read_root():
    logger.info('Отработал GET запрос')
    return {"Hello": "World"}


@app.post('/items/')
async def create_item(item: Item):
    logger.info('Отработан POST запрос')
    return item


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработан PUT запрос для item_id = {item_id}.')
    return {'item_id': item_id, 'item': item}


@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    logger.info(f'Отработан DELETE запрос для item_id = {item_id}.')
    return {'item_id': item_id}
