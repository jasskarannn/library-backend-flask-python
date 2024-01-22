from data.models.stores import StoreModel
from data.models.stores import StoreResponse


def store_response_converter(store: StoreModel) -> dict:
    if store is None:
        return {"error": "store not found"}
    else:
        return StoreResponse(
            id=store.id,
            name=store.name
        ).dict()
