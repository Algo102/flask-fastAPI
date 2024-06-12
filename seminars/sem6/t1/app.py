# Задание №1
# 📌 Разработать API для управления списком пользователей с
# использованием базы данных SQLite. Для этого создайте
# модель User со следующими полями:
# ○ id: int (идентификатор пользователя, генерируется автоматически)
# ○ username: str (имя пользователя)
# ○ email: str (электронная почта пользователя)
# ○ password: str (пароль пользователя)
# 📌 API должно поддерживать следующие операции:
# ○ Получение списка всех пользователей: GET /users/
# ○ Получение информации о конкретном пользователе: GET /users/{user_id}/
# ○ Создание нового пользователя: POST /users/
# ○ Обновление информации о пользователе: PUT /users/{user_id}/
# ○ Удаление пользователя: DELETE /users/{user_id}/
# 📌 Для валидации данных используйте параметры Field модели User.
# 📌 Для работы с базой данных используйте SQLAlchemy и модуль databases.

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
