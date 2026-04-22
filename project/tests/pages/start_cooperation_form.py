from selenium.webdriver.common.by import By

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.elements.button import Button


class StartCooperationForm(Form):
    __callback_button = Button(
        Locator(By.CSS_SELECTOR, ".button.callback_icon"), 
        "Callback"
    )
    __user_name_input = TextBox(
        Locator(By.ID, "POPUP_NAME"), 
        "User name"
    )
    __user_phone_number_input = TextBox(
        Locator(By.ID, "POPUP_PHONE"), 
        "User phone number"
    )
    __needed_service_name_input = TextBox(
        Locator(By.ID, "POPUP_NEED_PRODUCT"), 
        "Needed service name"
    )
    __user_message_input = TextBox(
        Locator(By.ID, "POPUP_MESSAGE"),
        "User message"
    )

    def __init__(self):
        super().__init__(Locator(By.XPATH, "//form[@name='aspro_priority_question']"), "Start cooperation form")

    def wait_and_click_callback_button(self):
        self.__callback_button.wait_and_click()
    
    def input_user_name(self, user_name):
        self.__user_name_input.send_keys(user_name)

    def input_user_phone_number(self, phone_number):
        self.__user_phone_number_input.send_keys(phone_number)
    
    def input_needed_service_name(self, service_name):
        self.__needed_service_name_input.send_keys(service_name)
    
    def input_user_message(self, message):
        self.__user_message_input.send_keys(message)