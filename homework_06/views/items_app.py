from flask import Blueprint, render_template, request, url_for, redirect, flash

from models import db, Item
from views.forms.products import CreateItemForm

print("__name__", __name__)
items_app = Blueprint("items_app", __name__)  # аналог APIRouter в FastAPI


@items_app.route("/", endpoint="list")
def get_products():
    items = Item.query.all()
    # print(repr(products))
    # print(type(products))
    return render_template(
        "items/list.html", items=items
    )  # рендер темплита и передача продуктов в шаблон


@items_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = CreateItemForm()
    if request.method == "GET":
        return render_template("items/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("items/add.html", form=form), 400
    print(request.form)
    # product_name = request.form.get("product-name", "")
    # product_name = product_name.strip()
    # if not product_name:
    #     raise BadRequest("Field 'product-name' is required")

    item_name = (form.name.data)

    item = Item(name=item_name)
    db.session.add(item)
    db.session.commit()

    flash(f"Successfully added item {item.name}!")
    url = url_for("items_app.list")
    return redirect(url)
