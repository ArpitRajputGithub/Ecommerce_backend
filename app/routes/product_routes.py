from fastapi import APIRouter, status, Query
from typing import Optional
from app.models.product_model import ProductCreateModel
from app.services.product_service import create_product
from app.services.product_service import list_products

router = APIRouter()

@router.post("/products", status_code=status.HTTP_201_CREATED)
def add_product(product: ProductCreateModel):
    product_id = create_product(product)
    return {"id": product_id}

@router.get("/products")
def get_products(
    name: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    limit: int = Query(10, ge=0),
    offset: int = Query(0, ge=0)
):
    products = list_products(name=name, size=size, limit=limit, offset=offset)
    page = {
        "next": offset + limit,
        "limit": limit,
        "previous": max(offset - limit, 0)
    }
    return {"data": products, "page": page}
