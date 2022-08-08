# Сборка приложения: docker build . -t app
# Запуск контейнера с пробросом порта: docker run -p 8000:8000 -it app
# где первый порт - то, что видно снаружи, второй - внутри контейнера

FROM python:3.9-buster

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry==1.1.14
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY web-app .

EXPOSE 8000

CMD uvicorn app:app --host=0.0.0.0 --port=8000