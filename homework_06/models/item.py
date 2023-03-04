from .database import db
from sqlalchemy import Column, Integer, String


class Item(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
