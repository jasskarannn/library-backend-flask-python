from flask import request, Blueprint
import logging
from typing import Dict, Tuple
from services import healthcheck
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from data.models import ItemModel, StoreModel
from services.store_service import store_read_service, store_write_service, store_response_service
from services.item_service import item_read_service, item_write_service, item_response_service

router = Blueprint("router", __name__)
logger = logging.getLogger(__name__)


# to health check the service
@router.route("/ping", methods=["GET"])
def ping() -> Tuple[Dict, int]:
    connection_status = healthcheck.check_health()
    if connection_status["health_check_successful"] is not True:
        return connection_status, 503
    return connection_status, 200


# to get all stores
@router.route("/store", methods=["GET"])
def get_stores():
    return store_read_service.get_all_stores()


# to get a particular store from store_id
@router.route("/store/<string:store_id>", methods=["GET"])
def get_store(store_id: str):
    try:
        store = store_read_service.get_store(store_id)
        store_response = store_response_service.store_response_converter(store)
        return store_response, 200
    except KeyError:
        return "Store not found", 404


# to get an item from item_id
@router.route("/item/<string:item_id>", methods=["GET"])
def get_item(item_id: str):
    try:
        item = item_read_service.get_item(item_id)
        item_response = item_response_service.item_response_converter(item)
        return item_response, 200
    except KeyError:
        return "Item not found", 404


# to get all items
@router.route("/item", methods=["GET"])
def get_all_items():
    return item_read_service.get_all_items()


# to add store data
@router.route("/store", methods=["POST"])
def create_store():
    try:
        store_data = request.get_json()
        store = StoreModel(**store_data)
        store_write_service.create_store(store)
    except IntegrityError:
        return "Integrity error while adding store", 400
    except SQLAlchemyError:
        return "An error occurred while adding", 500
    except Exception as e:
        logger.error(f"unknown exception occurred while adding store: {e}")
        return "An error occurred while adding store", 500

    store_response = store_response_service.store_response_converter(store)
    return store_response, 201


# to add an item with a particular store_id to insert item into
@router.route("/item", methods=["POST"])
def create_item():
    try:
        item_data = request.get_json()
        item = ItemModel(**item_data)
        item_write_service.create_item(item)
    except SQLAlchemyError:
        return "An error occurred while adding item", 500
    except Exception as e:
        logger.error(f"unknown exception occurred while adding item: {e}")
        return "An error occurred while adding item", 500

    item_response = item_response_service.item_response_converter(item)
    return item_response, 201
