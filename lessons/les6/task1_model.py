from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None  # Можно было не писать, т.к. bool по умолчанию False


class User(BaseModel):
    username: str
    full_name: str = None  # Не обязательное поле


class Order(BaseModel):
    items: List[Item]  # Список из модели созданной ранее
    user: User
