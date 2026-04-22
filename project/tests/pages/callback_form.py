from selenium.webdriver.common.by import By

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.elements.button import Button

class CallbackForm(Form):
    __close_callback_form_button = Button(
        Locator(By.CSS_SELECTOR, ".callback_frame .jqmClose"),
        "Close side form"
    )
    __user_name_input = TextBox(Locator(By.ID, "POPUP_FIO"), "User name")
    __user_phone_number_input = TextBox(Locator(By.ID, "POPUP_PHONE"), "User phone number")

    def __init__(self):
        super().__init__(Locator(By.XPATH, "//form[@name='aspro_priority_callback']"), "Callback form")

    def wait_and_click_close_callback_form_button(self):
        self.__close_callback_form_button.wait_and_click()

    def input_user_name(self, user_name):
        self.__user_name_input.send_keys(user_name)
    
    def input_user_phone_number(self, phone_number):
        self.__user_phone_number_input.send_keys(phone_number)