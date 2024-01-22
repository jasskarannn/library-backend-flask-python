from data.models import StoreModel, ItemModel
from extensions import db
from sqlalchemy import desc


def create_store_in_db(store: StoreModel):
    db.session.add(store)
    db.session.commit()


def create_item_in_db(item: ItemModel):
    db.session.add(item)
    db.session.commit()


# functions to retrieve the latest store_id, item_id from database. New store/item in Redis will be stored
# against this value as it's 'key'.
# key in redis for item : ITEM_PREFIX + item_id
# key in redis for store : STORE_PREFIX + store_id
def get_latest_store_id():
    latest_store_row = db.session.execute(
        db.select(
            StoreModel.id
        ).order_by(
            desc(StoreModel.id)
        )
    ).first()

    latest_store_id = str(latest_store_row).replace('(', '').replace(')', '').replace(',', '')
    return latest_store_id


def get_latest_item_id():
    latest_item_row = db.session.execute(
        db.select(
            ItemModel.id
        ).order_by(
            desc(ItemModel.id)
        )
    ).first()

    latest_item_id = str(latest_item_row).replace('(', '').replace(')', '').replace(',', '')
    return latest_item_id
