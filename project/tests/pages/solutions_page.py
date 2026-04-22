from selenium.webdriver.common.by import By
from typing import List

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label
from py_selenium_auto.elements.link import Link

class SolutionsPage(Form):
    """
    Страница Решения 1C

    """
    __product_group_card_locator = Locator(By.XPATH, "//*[contains(@class,'item') and contains(@class,'left')]//*[contains(@class,'title')]//a")

    __product_group_card_locator_template = (
        By.XPATH,
        "//*[contains(@class,'item')]//a[contains(text(),'{}')]"
    )

    def __init__(self):
        super().__init__(Locator(By.ID, "pagetitle"), "1C Solutions page")

    def wait_and_click_first_1c_solution_card(self):
        cards = self._element_factory.find_elements(
            Link,
            self.__product_group_card_locator,
            "1C Solutions cards"
        )
        cards[0].wait_and_click()
    
    def get_1c_solutions(self) -> List[str]: 
        elements = self._element_factory.find_elements(
            Label,
            self.__product_group_card_locator,
            "1C Solutions titles"
        )
        return [element.get_text().strip() for element in elements]
    
    def wait_and_click_product_group_by_name(self, card_name: str) -> Link:
        by, xpath_template = self.__product_group_card_locator_template
        locator = Locator(by, xpath_template.format(card_name))
        product_group_card = Link(locator, f"Solution card with text={card_name}")
        product_group_card.wait_and_click()
