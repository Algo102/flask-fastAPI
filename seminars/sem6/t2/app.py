# Задание №2
# 📌 Создать веб-приложение на FastAPI, которое будет предоставлять API для
# работы с базой данных пользователей. Пользователь должен иметь
# следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)
# 📌 API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
# 📌 Приложение должно использовать базу данных SQLite3 для хранения
# пользователей.

from fastapi import FastAPI
import uvicorn
from db import database
# from seminars.sem6.t1.routers.users import router
from routers.users import router as router_users

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(router_users, tags=['users'])

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='localhost',
        port=8000,
        reload=True
    )
