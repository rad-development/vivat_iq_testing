from selenium.webdriver.common.by import By
from typing import List

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.link import Link
from py_selenium_auto.elements.label import Label

class ServicesPage(Form):
    __service_title_locator = Locator(By.CSS_SELECTOR, ".col-sm-12.info .title, .col-sm-12 h2")
    __service_arrow_link_locator = Locator(By.XPATH, "//a[@class='arrow_link' and contains(@href,'services')]")

    def __init__(self):
        super().__init__(
            Locator(By.ID, "pagetitle"),
            "Services page"
        )

    def get_services(self) -> List[str]: 
        elements = self._element_factory.find_elements(
            Label,
            self.__service_title_locator,
            "Service titles"
        )
        return [element.text.strip() for element in elements]
    
    def wait_and_click_first_service_link(self):
        links = self._element_factory.find_elements(
            Link,
            self.__service_arrow_link_locator,
            "Service links"
        )
        links[0].wait_and_click()