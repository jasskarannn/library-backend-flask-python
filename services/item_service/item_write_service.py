import logging
from services.db.db_write_service import create_item_in_db
from services.redis.redis_write_service import create_item_in_redis
from data.models import ItemModel

logger = logging.getLogger(__name__)


def create_item(item: ItemModel):
    create_item_in_db(item)
    create_item_in_redis(item)
