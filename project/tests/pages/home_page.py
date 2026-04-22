from selenium.webdriver.common.by import By
from typing import List

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.label import Label

class HomePage(Form):
    __service_title_label = Locator(By.CSS_SELECTOR, ".item.border .title")
    __project_container = Locator(By.CLASS_NAME, "col-md-4")
    __start_cooperation_button = Button(
        Locator(By.XPATH, "//*[@data-name='resume']"),
        "Start cooperation"
    )

    def __init__(self):
        super().__init__(Locator(By.CLASS_NAME, "services-items"), "Home page")

    def wait_and_click_start_cooperation_button(self):
        self.__start_cooperation_button.wait_and_click()

    def get_services(self) -> List[Label]: 
        return self._element_factory.find_elements(
            Label,
            self.__service_title_label,
            "Service title"
            )
    
    def get_projects(self) -> List[Label]: 
        return self._element_factory.find_elements(
            Label,
            self.__project_container,
            "Project"
            )
