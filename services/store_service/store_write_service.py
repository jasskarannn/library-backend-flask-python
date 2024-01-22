import logging
from services.db.db_write_service import create_store_in_db
from services.redis.redis_write_service import create_store_in_redis
from data.models import StoreModel

logger = logging.getLogger(__name__)


def create_store(store: StoreModel):
    create_store_in_db(store)
    create_store_in_redis(store)
