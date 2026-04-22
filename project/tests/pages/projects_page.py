from selenium.webdriver.common.by import By
from typing import List

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.label import Label

class ProjectsPage(Form):
    __project_title_locator = Locator(By.CSS_SELECTOR, ".col-sm-4 .title")
    __load_more_projects_button = Button(
        Locator(By.CLASS_NAME, "ajax_load_btn_pagination"),
        "Load more projects"
    )

    def __init__(self):
        super().__init__(Locator(By.XPATH, ""), "Projects page")

    def get_projects(self) -> List[Label]: 
        return self._element_factory.find_elements(
            Label,
            self.__project_title_locator,
            "Project title"
            )

    def wait_and_click_load_more_projects_button(self):
        self.__load_more_projects_button.wait_and_click()

    def wait_until_load_more_projects_button_is_invisible(self):
        return self.__load_more_projects_button.state.wait_for_not_displayed()