from pydantic import BaseModel
from typing import List

class SizeModel(BaseModel):
    size: str
    quantity: int

class ProductCreateModel(BaseModel):
    name: str
    price: float
    sizes: List[SizeModel]
