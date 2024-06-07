# Задание №2
# 📌 Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс Movie с полями id, title, description и genre.
# 📌 Создайте список movies для хранения фильмов.
# 📌 Создайте маршрут для получения списка фильмов по жанру (метод GET).
# 📌 Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, HTTPException
import logging
from pydantic import BaseModel
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Genre(BaseModel):
    id: int
    name: str


class Movie(BaseModel):
    id: int
    title: str
    discription: Optional[str] = None
    genre: Genre


movies = [
    Movie(id=0, title='Movie 0', discription='This', genre=Genre(id=0, name='horror')),
    Movie(id=1, title='Movie 1', discription='movie', genre=Genre(id=0, name='horror')),
    Movie(id=2, title='Movie 2', discription='is', genre=Genre(id=1, name='comedy')),
    Movie(id=3, title='Movie 3', discription='the', genre=Genre(id=0, name='horror')),
    Movie(id=4, title='Movie 4', discription='best', genre=Genre(id=2, name='drama')),
    Movie(id=5, title='Movie 5', discription='in', genre=Genre(id=0, name='horror')),
]


@app.get('/movies/', response_model=list[Movie])
async def get_movies(genre_id: int = None, genre_name=None):
    if genre_id is not None:
        return [movie for movie in movies if movie.genre.id == genre_id]
    if genre_name is not None:
        return [movie for movie in movies if movie.genre.name == genre_name]
    return movies


if __name__ == '__main__':
    uvicorn.run('task02:app', host='localhost', port=8000, reload=True)
