"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, request, render_template

from homework_05.about_app import about_app

app = Flask(__name__)

app.register_blueprint(about_app, url_prefix="/about")


def print_request():
    print(
        "request: ",
        request,
        " | request.method: ",
        request.method,
        " | request.path: ",
        request.path,
    )


@app.route("/", endpoint="index_page")
def index_view():
    print_request()
    return render_template("index.html")
