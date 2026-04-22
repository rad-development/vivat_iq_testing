import pytest
import pytest_check as SoftAssert
from py_selenium_auto_core.logging.logger import Logger

from tests.utils.test_data_manager import TestDataManager
from tests.test_cases.home_page_coop_form.coop_form_data_model import CoopFormDataModel
from tests.pages.home_page import HomePage
from tests.pages.start_cooperation_form import StartCooperationForm
from tests.pages.callback_form import CallbackForm

class TestHomePageCoopForm:
    test_data = TestDataManager.get_dataset(CoopFormDataModel)

    @pytest.mark.parametrize("user", test_data)
    def test_home_page_coop_form(self, user):
        Logger.info("Step 1: Verify that 'Services' and 'Projects' blocks are displayed on the homepage")
        home_page = HomePage() 
        assert home_page.state.is_displayed(), f"{home_page.name} is not displayed"

        SoftAssert.is_true(home_page.get_projects(),
            f"'Projects' block is not displayed on the {home_page.name}"
        )
        SoftAssert.is_true(home_page.get_services(), 
            f"'Services' block is not displayed on the {home_page.name}"
        )

        Logger.info("Step 2: Click the 'Start Cooperation' button in the 'About Company' block")
        home_page.wait_and_click_start_cooperation_button()

        Logger.info("Step 3: Fill out the 'Start Cooperation' form with name, phone, service, and message")
        coop_form = StartCooperationForm()
        assert coop_form.state.wait_for_displayed(), f"{coop_form.name} is not displayed"

        coop_form.input_user_name(user.user_name)
        coop_form.input_user_phone_number(user.user_phone_number)
        coop_form.input_needed_service_name(user.needed_service_name)
        coop_form.input_user_message(user.user_message)

        Logger.info("Step 4: Click the 'Request Callback' button in the 'Start Cooperation' form")
        coop_form.wait_and_click_callback_button()
        assert coop_form.state.wait_for_not_displayed(), (
            f"{coop_form.name} is still displayed after clicking 'Request Callback'"
        )

        Logger.info("Step 5: Fill out the 'Callback' form with name and phone")
        callback_form = CallbackForm()
        assert callback_form.state.wait_for_displayed(), f"{callback_form.name} is not displayed"

        callback_form.input_user_name(user.user_name)
        callback_form.input_user_phone_number(user.user_phone_number)     

        Logger.info("Step 6: Close the 'Callback' form using the close button")   
        callback_form.wait_and_click_close_callback_form_button()
        assert callback_form.state.wait_for_not_displayed(), (
            f"{callback_form.name} is still displayed after closing"
        )
