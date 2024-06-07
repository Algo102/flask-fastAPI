# Форматирование ответов API
# Для работы с HTML и с json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

app = FastAPI()


# Два допустимых варианта указания:
# в качестве параметра
@app.get('/', response_class=HTMLResponse)
async def read_root():
    return '<h1>Hello World!</h1>'


# В качестве возвращаемого объекта
@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)
