from extensions import db
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer, String


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    item = relationship("ItemModel", back_populates="store", lazy="dynamic")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class StoreResponse(BaseModel):
    id: int
    name: str


class StoreModelExtension(StoreModel, object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
