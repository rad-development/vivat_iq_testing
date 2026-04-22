from selenium.webdriver.common.by import By
from typing import List

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label
from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.link import Link

class ProductGroupPage(Form):
    """
    Страница Решения 1C ---> Группа товаров (допустим Кадровый учет)

    """
    __product_group_1c_name_label = Label(
        Locator(By.ID, "pagetitle"),
        "1C product group name")
    __ask_question_button = Button(
        Locator(By.XPATH, "//*[contains(@class,'detail_right_block')]//*[@data-name='question']"),
        "Ask a question about product")
    __product_card_locator = Locator(By.XPATH, "//*[contains(@class,'col-sm-4')]")
    __product_name_locator = Locator(By.XPATH, "//*[@class='item']//*[@itemprop='name']")
    __product_card_locator_template = (
        By.XPATH,
        "//*[@itemprop='name' and contains(text(),'{}')]"
    )

    def __init__(self):
        super().__init__(Locator(By.ID, "pagetitle"), "1C product group page")

    def get_product_group_name(self) -> str:
        return self.__product_group_1c_name_label.get_text().strip()
    
    def get_product_names(self) -> List[str]:
        elements = self._element_factory.find_elements(
            Label,
            self.__product_name_locator,
            "Service titles"
        )
        return [element.text.strip() for element in elements]
    
    def wait_and_click_ask_question_button(self):
        self.__ask_question_button.wait_and_click()
    
    def wait_and_click_first_product_card(self):
        cards = self._element_factory.find_elements(
            Link,
            self.__product_card_locator,
            "1C Solutions cards"
        )
        cards[0].wait_and_click()

    def wait_and_click_product_card_by_name(self, card_name: str) -> Link:
        by, xpath_template = self.__product_card_locator_template
        locator = Locator(by, xpath_template.format(card_name))
        product_group_card = Link(locator, f"Product card with name={card_name}")
        product_group_card.wait_and_click()
