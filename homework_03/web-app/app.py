"""
API - application programming interface
"""
from fastapi import FastAPI

from views import router as ping_router

app = FastAPI()  # Framework, который позволят очень быстро писать API (минимум усилий на приложение
                    # с возможноестью отправлять запросы)

app.include_router(ping_router)

@app.get("/")   # приложение, которое умеет обрабатывать запросы / декоратор разрешает только GET, при отправке
                # POST будет ошибка. "/" - запрос на корень
def root():
    return {"message": "Let's play ping pong"}

## ТЕСТ на http://127.0.0.1:8000/docs#/ при проброске порта 8000
