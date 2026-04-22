from selenium.webdriver.common.by import By

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.elements.button import Button
from selenium.webdriver.common.keys import Keys

class ProductPage(Form):
    __product_name_label = Label(
        Locator(By.ID, "pagetitle"),
        "1C product name")
    __amount_of_product_input = TextBox(
        Locator(By.CSS_SELECTOR, ".counter input"),
        "Selected amount of product"
    )
    __add_to_cart_button = Button(
        Locator(By.CLASS_NAME, "to_cart"),
        "Add product to cart"
    )

    def __init__(self):
        super().__init__(Locator(By.ID, "pagetitle"), "1C product page")

    def get_product_name(self) -> str:
        return self.__product_name_label.get_text().strip()
    
    def wait_and_set_product_amount_to(self, amount: int):
        element = self.__amount_of_product_input
        element.wait_and_click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(str(amount))
    
    def wait_and_click_add_to_cart_button(self):
        self.__add_to_cart_button.wait_and_click()
