# Задание №6
# 📌 Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс User с полями id, name, email и password.
# 📌 Создайте список users для хранения пользователей.
# 📌 Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# 📌 Создайте маршрут для отображения списка пользователей (метод GET).
# 📌 Реализуйте вывод списка пользователей через шаблонизатор Jinja.

from typing import Optional

import uvicorn
from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import logging
from pydantic import BaseModel, field_validator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = [User(id=1, name='test', email='zapros@za.ru', password='qweqweqwe')]


@app.get('/users/')
def get_users(request: Request):
    return templates.TemplateResponse('index.html', {"request": request, 'users': users})


@app.post('/users/')
def add_user(
        request: Request,
        id: Annotated[int, Form()],
        name: Annotated[str, Form()],
        email: Annotated[str, Form()],
        password: Annotated[str, Form()]
):
    users.append(User(id=id, name=name, email=email, password=password))
    return templates.TemplateResponse('index.html', {"request": request, 'users': users})


if __name__ == '__main__':
    uvicorn.run('task06:app', host='localhost', port=8000, reload=True)
