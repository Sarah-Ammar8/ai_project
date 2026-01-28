from .errors import NotFoundError


def get_item(item_id: int) -> dict:
    """
    مثال لمنطق أعمال بسيط:
    إذا لم يوجد العنصر، نرمي NotFoundError
    """
    fake_database = {
        1: {"id": 1, "name": "Item One"},
        2: {"id": 2, "name": "Item Two"},
    }

    if item_id not in fake_database:
        raise NotFoundError(
            message="Item not found",
            details={"item_id": item_id}
        )

    return fake_database[item_id]
