# Документация http://127.0.0.1:8000/docs - лучше для интерактивного тестирования
# Альтернатива http://127.0.0.1:8000/redoc - более наглядно, но без тестирования

# Для генерации документации нужно создать экземпляр класса FastAPI с
# параметром openapi_url:
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(openapi_url="/api/v1/openapi.json")


@app.get("/hello/{name}")
async def read_item(name: str, age: int):
    return {"Hello": name, "Age": age}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi