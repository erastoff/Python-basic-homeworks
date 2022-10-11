#FROM python:3.10-bullseye
#
#WORKDIR /app
#
#COPY requirements.txt .
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

FROM tiangolo/uwsgi-nginx-flask:python3.10
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
