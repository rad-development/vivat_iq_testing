from selenium.webdriver.common.by import By

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label
from py_selenium_auto.elements.link import Link

class NavigationHeader(Form):
    __services_link = Link(
        Locator(By.CSS_SELECTOR, ".header_container a[href='/services/']"),
        "Services")
    __projects_link = Link(
        Locator(By.CSS_SELECTOR, ".header_container a[href='/projects/'].dropdown-toggle"),
        "Services")
    __solutions_link = Link(
        Locator(By.CSS_SELECTOR,".header_container .menu-item a[href='/product/']"),
        "1C Solutions")
    __vivat_solutions_link = Link(
        Locator(By.XPATH,"//*[contains(@class,'header_container')]//a[contains(@href, 'vivat')]"),
        "VIVAT-IQ Solutions")
    __cart_item_counter_label = Label(
        Locator(By.CSS_SELECTOR, ".header_container .basket-link .count"),
        "Cart item counter"
    )
    __cart_link = Link(
        Locator(By.CSS_SELECTOR, ".header_container .basket-link"),
        "Cart"
    )
    __cart_make_order_link = Link(
        Locator(By.XPATH, "//*[contains(@class,'header_wrap')]//a[@href='/cart/order/']"),
        "Cart make order"
    )

    def __init__(self):
        super().__init__(Locator(By.XPATH, "//*[contains(@class,'header_container')]"), "Navigation header")
    
    def wait_and_click_services_link(self):
        self.__services_link.wait_and_click()

    def wait_and_click_projects_link(self):
        self.__projects_link.wait_and_click()
    
    def wait_and_click_1c_solutions_link(self):
        self.__solutions_link.wait_and_click()

    def wait_and_click_vivat_solutions_link(self):
        self.__vivat_solutions_link.wait_and_click()

    def get_cart_item_count(self) -> int: 
        num_of_items = self.__cart_item_counter_label.get_text()
        return int(num_of_items)
    
    def wait_and_click_cart_icon(self):
        self.__cart_link.wait_and_click()

    def wait_for_cart_make_order_popup(self):
        self.__cart_make_order_link.state.wait_for_displayed()