from app.models.order_model import OrderCreateModel
from app.config.db import get_order_collection
from app.config.db import get_product_collection
from bson import ObjectId

def create_order(order_data: OrderCreateModel):
    order_dict = order_data.dict()
    # Convert productId to ObjectId for each item
    for item in order_dict["items"]:
        try:
            item["productId"] = ObjectId(item["productId"])
        except Exception:
            pass
    result = get_order_collection().insert_one(order_dict)
    print("Order insert result:", result.inserted_id)
    return str(result.inserted_id)

def get_orders_by_user(user_id: str, limit: int = 10, offset: int = 0):
    collection = get_order_collection()
    pipeline = [
        {"$match": {"userId": user_id}},
        {"$sort": {"_id": -1}},
        {"$skip": offset},
        {"$limit": limit},
        {"$unwind": "$items"},
        {
            "$lookup": {
                "from": "products",
                "let": {"pid": "$items.productId"},
                "pipeline": [
                    {"$match": {"$expr": {"$eq": ["$_id", "$$pid"]}}}
                ],
                "as": "productDetails"
            }
        },
        {"$unwind": "$productDetails"},
        {
            "$group": {
                "_id": "$_id",
                "items": {"$push": {
                    "productDetails": {
                        "id": {"$toString": "$productDetails._id"},
                        "name": "$productDetails.name"
                    },
                    "qty": "$items.qty"
                }},
                "total": {"$sum": {"$multiply": ["$items.qty", "$productDetails.price"]}}
            }
        },
        {"$project": {
            "_id": 0,
            "id": {"$toString": "$_id"},
            "items": 1,
            "total": 1
        }}
    ]
    orders = list(collection.aggregate(pipeline))
    return orders
