__all__ = ("db",)

from typing import TYPE_CHECKING, Type

from flask_sqlalchemy import BaseQuery
from flask_sqlalchemy import SQLAlchemy as SQLAlchemyGeneric, Model
from sqlalchemy.orm import Session


class Base(Model):
    if TYPE_CHECKING:
        query: "BaseQuery"


class SQLAlchemy(SQLAlchemyGeneric):
    if TYPE_CHECKING:
        Model = Type[Base]
        session: Session


db: "SQLAlchemy" = SQLAlchemy(model_class=Base)
