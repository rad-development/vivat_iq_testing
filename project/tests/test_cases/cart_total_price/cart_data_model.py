from pydantic import BaseModel
from typing import Optional

from tests.utils.test_data_path_helper import TestDataPathHelper


class CartDataModel(BaseModel):
    cart_item_count_initial: Optional[int] = None
    cart_item_count_after_adding: Optional[int] = None
    cart_is_empty_message: Optional[str] = None
    product_group_name: Optional[str] = None
    product_name: Optional[str] = None
    amount_of_product: Optional[int] = None

    @classmethod
    def data_file(cls):
        return TestDataPathHelper.get_test_data_file_path(
            TC_folder_name="cart_total_price",
            filename="cart_test_data.json"
        )
    