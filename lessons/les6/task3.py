from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., title="Name", max_length=50)  # ... - поле обязательное для заполнения
    price: float = Field(..., title="Price", gt=0, le=100000)
    description: str = Field(default=None, title="Description", max_length=1000)  # - по умолчанию None, т.е. поле не обязательное
    tax: float = Field(0, title="Tax", ge=0, le=10)  # - можно не указывать default


class User(BaseModel):
    username: str = Field(title="Username", max_length=50)
    full_name: str = Field(None, title="Full Name", max_length=100)