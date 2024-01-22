import logging
from services.db import db_read_service
from services.redis import redis_read_service, redis_write_service
from services.db.db_read_service import get_all_stores_from_db
logger = logging.getLogger(__name__)


def get_store(store_id: str):
    try:
        store_result = redis_read_service.get_cached_store(store_id)
        if store_result is not None:
            return store_result
        else:
            logger.info("[get_store] Store data not in redis, fetching from database.")
            store_result = db_read_service.get_store(store_id)
            redis_write_service.create_store_in_redis(store_result)
            return store_result
    except Exception as e:
        logger.error("[get_store] Unknown exception occurred: ", e)


def get_all_stores():
    return get_all_stores_from_db()