import re
from selenium.webdriver.common.by import By

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label
from py_selenium_auto.elements.button import Button
from src.models.cart_item_model import CartItemModel

class CartPage(Form):
    __empty_basket_message_label = Label(
        Locator(By.CLASS_NAME, "basket_empty"),
        "empty basket message")
    __to_catalog_button = Button(
        Locator(By.CSS_SELECTOR, ".basket_empty .btn"),
        "Go to catalog")
    __remove_all_items_button = Button(
        Locator(By.CSS_SELECTOR, ".remove.all"),
        "Remove all items from cart")
    __item_locator = Locator(By.CSS_SELECTOR, ".basket .item")
    __item_name_locator = Locator(By.CSS_SELECTOR, ".name a")
    __item_individual_price_locator = Locator(By.XPATH, "//*[@class='prices box']//*[@class='price_val']")
    __item_total_price_locator = Locator(By.CSS_SELECTOR, ".summ .price_val")
    __item_count_locator = Locator(By.CSS_SELECTOR, ".count")
    __total_sum_of_all_items_label = Label(
        Locator(By.CSS_SELECTOR, ".total span"),
        "Total price of all items in the cart")


    def __init__(self):
        super().__init__(Locator(By.ID, "pagetitle"), "Cart page")

    def wait_and_get_empty_basket_message_text(self):
        self.__empty_basket_message_label.state.wait_for_displayed()
        return self.__empty_basket_message_label.get_text()
    
    def wait_and_click_to_catalog_button(self):
        self.__to_catalog_button.wait_and_click()

    def wait_and_click_remove_all_items_button(self):
        self.__remove_all_items_button.wait_and_click()

    def __parse_price(self, text: str) -> float:
        cleaned = re.sub(r"[^\d.,]", "", text)
        cleaned = cleaned.replace(",", ".")
        return float(cleaned)

    def get_items_in_cart(self):
        items_container = Label(self.__item_locator, "Cart items")
        items_container.state.wait_for_displayed()
        items = self._element_factory.find_elements(
            Label,
            self.__item_locator,
            "Cart item"
        )
        list_of_items = []
        for item in items:
            name_element = item.find_child_element(
                Label,
                self.__item_name_locator,
                "Item name"
            )
            price_element = item.find_child_element(
                Label,
                self.__item_individual_price_locator,
                "Item price for single"
            )
            total_price_element = item.find_child_element(
                Label,
                self.__item_total_price_locator,
                "Item total price"
            )
            count_element = item.find_child_element(
                Label,
                self.__item_count_locator,
                "Item count"
            )
            name = name_element.get_text()
            price_text = price_element.get_text()
            total_price_text = total_price_element.get_text()
            count = int(count_element.get_attribute("value"))

            price = self.__parse_price(price_text)
            total_price = self.__parse_price(total_price_text)

            cart_item = CartItemModel(
                name=name,
                price_for_single_item=price,
                amount=count,
                total_price=total_price
            )
            list_of_items.append(cart_item)

        return list_of_items
    
    def get_total_price_of_all_items_in_cart(self):
        summ_text = self.__total_sum_of_all_items_label.get_text()
        summ = self.__parse_price(summ_text)
        return summ