# Документация http://127.0.0.1:8000/docs - лучше для интерактивного тестирования
# Альтернатива http://127.0.0.1:8000/redoc - более наглядно, но без тестирования

from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
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
