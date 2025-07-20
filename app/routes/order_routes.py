from fastapi import APIRouter, status, Query
from app.models.order_model import OrderCreateModel
from app.services.order_service import create_order
from typing import Optional
from app.services.order_service import get_orders_by_user

router = APIRouter()

@router.post("/orders", status_code=status.HTTP_201_CREATED)
def add_order(order: OrderCreateModel):
    order_id = create_order(order)
    return {"id": order_id}

@router.get("/orders/{user_id}")
def get_orders(user_id: str, limit: int = Query(10, ge=0), offset: int = Query(0, ge=0)):
    orders = get_orders_by_user(user_id, limit=limit, offset=offset)
    page = {
        "next": offset + limit,
        "limit": limit,
        "previous": max(offset - limit, 0)
    }
    return {"data": orders, "page": page}
