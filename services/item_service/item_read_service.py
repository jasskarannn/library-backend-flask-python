import logging
from services.db import db_read_service
from services.redis import redis_read_service, redis_write_service
from services.db.db_read_service import get_all_items_from_db

logger = logging.getLogger(__name__)


def get_item(item_id: str):
    try:
        item_result = redis_read_service.get_cached_item(item_id)
        if item_result is not None:
            return item_result
        else:
            logger.info("[get_item] Item data not in redis, fetching from database.")
            item_result = db_read_service.get_item(item_id)
            redis_write_service.create_item_in_redis(item_result)
            return item_result
    except Exception as e:
        logger.error("[get_item] Unknown exception occurred: ", e)


def get_all_items():
    return get_all_items_from_db()
