from os import getenv

from flask import Flask, request, render_template
from flask_migrate import Migrate

from views.items_app import items_app

from models import db

app = Flask(__name__)

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

db.app = app  # db = SQLAlchemy(app) - в документации, но мы вынемли это в отдельный модуль - models
db.init_app(app)  # инициализация приложения под базу данных db
migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(items_app, url_prefix="/items")


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


@app.route("/items/", endpoint="items")
def get_items():
    return render_template("items/list.html")
