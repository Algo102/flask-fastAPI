from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(max_length=10)


class User(BaseModel):
    age: int = Field(default=0)


# Перечень принимаемых для функции Field параметров, Path - адреса, Query - ключ-значение
# Для валидации данных можно использовать следующие параметры при создании
# моделей:
# ● default: значение по умолчанию для поля
# ● alias: альтернативное имя для поля (используется при сериализации и
# десериализации)
# ● title: заголовок поля для генерации документации API
# ● description: описание поля для генерации документации API
# ● gt: ограничение на значение поля (д.б. больше указанного значения)
# ● ge: ограничение на значение поля (д.б. больше или равно указанному значению)
# ● lt: ограничение на значение поля (д.б. меньше указанного значения)
# ● le: ограничение на значение поля (д.б. меньше или равно указанному значению)
# ● multiple_of: ограничение на значение поля (должно быть кратно указанному
# значению)
# ● max_length: ограничение на максимальную длину значения поля
# ● min_length: ограничение на минимальную длину значения поля
# ● regex: регулярное выражение, которому должно соответствовать значение поля