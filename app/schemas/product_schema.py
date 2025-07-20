from bson import ObjectId

def product_schema(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "sizes": product["sizes"]
    }
