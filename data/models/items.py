from extensions import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer, String, Float


class ItemModel(db.Model):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String)
    price = Column(Float(precision=2), unique=False, nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    store = relationship("StoreModel", back_populates="item")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    store_id: str


class ItemModelExtension(ItemModel, object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
