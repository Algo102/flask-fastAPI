# Задание №3
# 📌 Создать API для управления списком задач.
# 📌 Каждая задача должна содержать поля "название",
# "описание" и "статус" (выполнена/не выполнена).
# 📌 API должен позволять выполнять CRUD операции с
# задачами.

# Задание №4
# 📌 Напишите API для управления списком задач. Для этого создайте модель Task
# со следующими полями:
# ○ id: int (первичный ключ)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)
# Задание №4 (продолжение)
# 📌 API должно поддерживать следующие операции:
# ○ Получение списка всех задач: GET /tasks/
# ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
# ○ Создание новой задачи: POST /tasks/
# ○ Обновление информации о задаче: PUT /tasks/{task_id}/
# ○ Удаление задачи: DELETE /tasks/{task_id}/
# 📌 Для валидации данных используйте параметры Field модели Task.
# 📌 Для работы с базой данных используйте SQLAlchemy и модуль databases.


from fastapi import FastAPI
import uvicorn
from db import database
from routers.tasks import router as router_tasks

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(router_tasks, tags=['tasks'])

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='localhost',
        port=8000,
        reload=True
    )
