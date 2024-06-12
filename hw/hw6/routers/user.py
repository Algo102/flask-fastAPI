from fastapi import APIRouter, HTTPException
from db import *
from models.models import *
from typing import List
from datetime import datetime

router = APIRouter()


@router.post("/users/", response_model=UserOut)
async def create_user(user: UserCreate):
    query = users.insert().values(username=user.username, email=user.email, password=user.password)
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}


@router.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/", response_model=List[UserOut])
async def read_users(skip: int = 0, limit: int = 10):
    query = users.select().offset(skip).limit(limit)
    return await database.fetch_all(query)


@router.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserCreate):
    query = users.update().where(users.c.id == user_id).values(username=user.username, email=user.email,
                                                               password=user.password)
    await database.execute(query)
    return {**user.dict(), "id": user_id}


@router.delete("/users/{user_id}", response_model=UserOut)
async def delete_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_query = users.delete().where(users.c.id == user_id)
    await database.execute(delete_query)
    return user


@router.post("/products/", response_model=ProductOut)
async def create_product(product: ProductCreate):
    query = products.insert().values(name=product.name, description=product.description, price=product.price)
    product_id = await database.execute(query)
    return {**product.dict(), "id": product_id}


@router.get("/products/{product_id}", response_model=ProductOut)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    product = await database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/products/", response_model=List[ProductOut])
async def read_products(skip: int = 0, limit: int = 10):
    query = products.select().offset(skip).limit(limit)
    return await database.fetch_all(query)


@router.put("/products/{product_id}", response_model=ProductOut)
async def update_product(product_id: int, product: ProductCreate):
    query = products.update().where(products.c.id == product_id).values(name=product.name,
                                                                        description=product.description,
                                                                        price=product.price)
    await database.execute(query)
    return {**product.dict(), "id": product_id}


@router.delete("/products/{product_id}", response_model=ProductOut)
async def delete_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    product = await database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    delete_query = products.delete().where(products.c.id == product_id)
    await database.execute(delete_query)
    return product


@router.post("/orders/", response_model=OrderOut)
async def create_order(order: OrderCreate):
    now = datetime.now()
    query = orders.insert().values(
        user_id=order.user_id,
        product_id=order.product_id,
        order_date=now,
        status="Pending"
    )
    order_id = await database.execute(query)
    return {**order.dict(), "id": order_id, "order_date": now, "status": "Pending"}


@router.get("/orders/{order_id}", response_model=OrderOut)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    order = await database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.get("/orders/", response_model=List[OrderOut])
async def read_orders(skip: int = 0, limit: int = 10):
    query = orders.select().offset(skip).limit(limit)
    return await database.fetch_all(query)


@router.put("/orders/{order_id}", response_model=OrderOut)
async def update_order(order_id: int, order: OrderCreate):
    now = datetime.now()
    values = {
        "user_id": order.user_id,
        "product_id": order.product_id,
        "order_date": now,
    }
    if order.status is not None:
        values["status"] = order.status

    query = orders.update().where(orders.c.id == order_id).values(values)
    await database.execute(query)
    updated_order = await database.fetch_one(orders.select().where(orders.c.id == order_id))
    return updated_order


@router.delete("/orders/{order_id}", response_model=OrderOut)
async def delete_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    order = await database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    delete_query = orders.delete().where(orders.c.id == order_id)
    await database.execute(delete_query)
    return order
