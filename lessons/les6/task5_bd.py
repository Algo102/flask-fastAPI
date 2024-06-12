# pip install sqlalchemy
# pip install databases[aiosqlite]

import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "sqlite:///mydatabase.db"  # в корневой папке создаем БД
# DATABASE_URL = "postgresql:///user:password@localhost/dbname"

database = databases.Database(DATABASE_URL)  # переменная для работы с БД
metadata = sqlalchemy.MetaData()

...

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Создание API операций CRUD
# Обсудим, как создать API операций CRUD (создание, чтение, обновление и
# удаление) с использованием FastAPI и SQLAlchemy ORM.
# Операции CRUD — это основные функции, которые используются в любом
# приложении, управляемом базой данных. Они используются для создания, чтения,
# обновления и удаления данных из базы данных. В FastAPI с SQLAlchemy ORM мы
# можем создавать эти операции, используя функции и методы Python.
# ● CREATE, Создать: добавление новых записей в базу данных.
# ● READ, Чтение: получение записей из базы данных.
# ● UPDATE, Обновление: изменение существующих записей в базе данных.
# ● DELETE, Удалить: удаление записей из базы данных.
