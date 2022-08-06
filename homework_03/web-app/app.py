"""
API - application programming interface
"""
from fastapi import FastAPI

app = FastAPI() # Framework, который позволят очень быстро писать API (минимум усилий на приложение
                # с возможноестью отправлять запросы)

@app.get("/")   # приложение, которое умеет обрабатывать запросы / декоратор разрешает только GET, при отправке
                # POST будет ошибка. "/" - запрос на корень сайта
def root():
    return {"message": "Let's play ping pong"}

@app.get("/ping") # обработка запроса на получение тела по адресу "/ping"
def ping():
    return {"message": "pong"}

## ТЕСТ на http://127.0.0.1:8000/docs#/Users/
