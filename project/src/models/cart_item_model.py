from pydantic import BaseModel
from typing import Optional

class CartItemModel(BaseModel):
    name: Optional[str] = None
    price_for_single_item: Optional[int] = None
    amount: Optional[int] = None
    total_price: Optional[int] = None
