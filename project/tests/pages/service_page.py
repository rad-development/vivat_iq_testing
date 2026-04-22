from selenium.webdriver.common.by import By

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label

class ServicePage(Form):
    __service_name_in_breadcrumbs = Label(
        Locator(By.XPATH, "//li[@class='active']//*[@itemprop='name']"),
        "Service name")

    def __init__(self):
        super().__init__(Locator(By.XPATH, ""), "Service page")

    def get_service_name_from_breadcrumbs(self):
        name = self.__service_name_in_breadcrumbs.text
        return name.lower().strip()