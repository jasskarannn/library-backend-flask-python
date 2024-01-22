import ast

from data.models import StoreModelExtension, ItemModelExtension
from extensions import redis_client
from constants import STORE_PREFIX, ITEM_PREFIX


def get_cached_store(store_id: str):
    key = STORE_PREFIX + store_id
    val = redis_client.get(key)
    if val is not None:
        string_val = val.decode('utf-8')
        dict_obj = ast.literal_eval(string_val)
        result_store = StoreModelExtension(dict_obj)
        return result_store
    else:
        return None


def get_cached_item(item_id: str):
    key = ITEM_PREFIX + item_id
    val = redis_client.get(key)
    if val is not None:
        string_val = val.decode('utf-8')
        dict_obj = ast.literal_eval(string_val)
        result_item = ItemModelExtension(dict_obj)
        return result_item
    else:
        return None
