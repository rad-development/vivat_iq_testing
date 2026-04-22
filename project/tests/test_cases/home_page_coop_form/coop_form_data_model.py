from pydantic import BaseModel
from typing import Optional

from tests.utils.test_data_path_helper import TestDataPathHelper


class CoopFormDataModel(BaseModel):
    user_name: Optional[str] = None
    user_phone_number: Optional[str] = None
    needed_service_name: Optional[str] = None
    user_message: Optional[str] = None

    @classmethod
    def data_file(cls):
        return TestDataPathHelper.get_test_data_file_path(
            TC_folder_name="home_page_coop_form",
            filename="coop_form_test_data.json"
        )
    