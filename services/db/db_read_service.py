import logging
from extensions import db
from data.models import StoreModel, ItemModel


logger = logging.getLogger(__name__)


def get_store(store_id: str) -> StoreModel:
    return db.session.query(StoreModel).filter_by(id=store_id).first()


def get_item(item_id: str) -> ItemModel:
    return db.session.query(ItemModel).filter_by(id=item_id).first()


def get_all_stores_from_db():
    store_results = db.session.execute(
        db.select(
                StoreModel.id,
                StoreModel.name
        )
    ).fetchall()

    stores = []
    for store in store_results:
        stores.append([x for x in store])
    return stores


def get_all_items_from_db():
    item_results = db.session.execute(
        db.select(
                ItemModel.id,
                ItemModel.name,
                ItemModel.price,
                ItemModel.store_id
        )
    ).fetchall()

    items = []
    for item in item_results:
        items.append([x for x in item])
    return items
