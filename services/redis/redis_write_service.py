import logging
from data.models import StoreModel, ItemModel
from extensions import redis_client
from constants import STORE_PREFIX, ITEM_PREFIX
from services.db.db_write_service import get_latest_store_id, get_latest_item_id
from services import ttl

logger = logging.getLogger(__name__)


def create_store_in_redis(store: StoreModel):
    if store is None:
        logger.info("[create_store_in_redis] Store doesn't exist in database, hence not storing in redis.")
        return

    store_id = get_latest_store_id()
    key = STORE_PREFIX + store_id
    value_as_string = str(store.as_dict())
    redis_client.setex(name=key, value=value_as_string, time=ttl)


def create_item_in_redis(item: ItemModel):
    if item is None:
        logger.info("[create_item_in_redis] Item doesn't exist in database, hence not storing in redis.")
        return

    item_id = get_latest_item_id()
    key = ITEM_PREFIX + item_id
    value_as_string = str(item.as_dict())
    redis_client.setex(name=key, value=value_as_string, time=ttl)

