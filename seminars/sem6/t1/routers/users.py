from fastapi import APIRouter, HTTPException
# from seminars.sem6.t1.db import database, users
from db import database, users
# from seminars.sem6.t1.models.users import User
from models.users import User, UserIn

router = APIRouter()


@router.get('/users/', response_model=list[User])
async def get_users():
    users_ = users.select()
    return await database.fetch_all(users_)


@router.post('/users/')
async def add_user(user: UserIn):
    query = users.insert().values(username=user.username, email=user.email, password=user.password)
    await database.execute(query)
    return {'msg': 'User added'}


@router.get('/users/{id}', response_model=User)
async def get_user(id: int):
    query = users.select().where(users.c.id == id)
    result = await database.fetch_one(query)
    if result:
        return result
    raise HTTPException(status_code=404, detail='User not found')


@router.put('/users/{id}', response_model=User)
async def update_user(id: int, user: UserIn):
    query = users.update().where(users.c.id == id).values(**user.dict())
    result = await database.execute(query)
    if result:
        return {**user.dict(), 'id': id}
    raise HTTPException(status_code=404, detail='User not found')


@router.delete('/users/')
async def delete_user(id: int):
    query = users.delete().where(users.c.id == id)
    result = await database.execute(query)
    if result:
        return {'msg': 'User deleted'}
    raise HTTPException(status_code=404, detail='User not found')