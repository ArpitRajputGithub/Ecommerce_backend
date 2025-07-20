from app.models.product_model import ProductCreateModel
from app.config.db import get_product_collection
from bson import ObjectId
from typing import Optional, List
from pymongo.collection import Collection

def create_product(product_data: ProductCreateModel):
    product_dict = product_data.dict()
    result = get_product_collection().insert_one(product_dict)
    return str(result.inserted_id)

def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
) -> List[dict]:
    collection: Collection = get_product_collection()
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size
    cursor = collection.find(query, {"sizes": 0}).skip(offset).limit(limit)
    products = []
    for product in cursor:
        products.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"]
        })
    return products
