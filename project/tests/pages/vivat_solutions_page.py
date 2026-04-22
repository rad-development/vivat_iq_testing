import re
from typing import List
from selenium.webdriver.common.by import By

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label
from py_selenium_auto.elements.link import Link
import time
from py_selenium_auto.browsers.browser_services import BrowserServices
from selenium.webdriver import ActionChains

class VivatSolutionsPage(Form):
    """
    Страница Решения Vivat-IQ

    """
    __product_locator = Locator(By.XPATH, "//*[contains(@class,'item-wrap')]")
    __product_title_locator = Locator(By.XPATH, "//*[contains(@class,'item-wrap')]//*[@class='title']")
    __product_price_locator = Locator(By.XPATH, "//*[contains(@class,'item-wrap')]//*[@class='price_val']")
    __sort_drop_down_menu_label = Label(Locator(By.CLASS_NAME, "sort_desktop"), "Sort by...")
    __sort_drop_down_menu_item_link = Link(Locator(By.XPATH, "//*[@class='dropdown']//*[contains(@class,'ordering')]"), "sorting option")
    __sort_by_price_ascending_link = Link(
        Locator(By.XPATH, "//*[contains(@class,'ordering')]//*[contains(@href,'FILTER_PRICE&order=asc')]"), 
        "sort by price ascending"
    )
    __sort_by_price_descending_link = Link(
        Locator(By.XPATH, "//*[contains(@class,'ordering')]//*[contains(@href,'FILTER_PRICE&order=desc')]"), 
        "sort by price descending"
    )
    def __init__(self):
        super().__init__(Locator(By.ID, "pagetitle"), "Vivat Solutions page")

    def get_vivat_iq_solutions_titles(self) -> List[str]: 
        elements = self._element_factory.find_elements(
            Label,
            self.__product_title_locator,
            "VIVAT-IQ Solutions titles"
        )
        return [element.get_text().strip() for element in elements]
    
    def __parse_price(self, text: str) -> float:
        cleaned = re.sub(r"[^\d.,]", "", text)
        cleaned = cleaned.replace(",", ".")
        return float(cleaned)

    def get_all_prices(self) -> List[float]:
        price_elements = self._element_factory.find_elements(
            Label,
            self.__product_price_locator,
            "Product prices"
        )
        prices = []
        for element in price_elements:
            text = element.get_text()
            prices.append(self.__parse_price(text))
        return prices
    
    def __open_sort_dropdown(self):
        self.__sort_drop_down_menu_label.state.wait_for_displayed()
        element = self.__sort_drop_down_menu_label.get_element()
        ActionChains(BrowserServices.Instance.browser.driver) \
            .move_to_element(element) \
            .perform()
        self.__sort_drop_down_menu_item_link.state.wait_for_displayed()

    def __select_sort_option(self, option: Link):
        self.__open_sort_dropdown()
        option.state.wait_for_clickable()
        option.wait_and_click()

    def sort_by_price_ascending(self):
        self.__select_sort_option(self.__sort_by_price_ascending_link)

    def sort_by_price_descending(self):
        self.__select_sort_option(self.__sort_by_price_descending_link)
