from data.models.items import ItemModel
from data.models.items import ItemResponse


def item_response_converter(item: ItemModel) -> dict:
    if item is None:
        return {"error": "item not found"}
    else:
        return ItemResponse(
            id=item.id,
            name=item.name,
            price=item.price,
            store_id=item.store_id
        ).dict()
