def order_schema(order) -> dict:
    return {
        "id": str(order["_id"]),
        "userId": order["userId"],
        "items": order["items"]
    }
