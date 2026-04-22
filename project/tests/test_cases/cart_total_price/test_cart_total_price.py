import pytest_check as soft_assert
from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto.browsers.browser_services import BrowserServices

from tests.utils.test_data_manager import TestDataManager
from tests.pages.navigation_header import NavigationHeader
from tests.pages.cart_page import CartPage
from tests.pages.product_group_page import ProductGroupPage
from tests.pages.product_page import ProductPage
from tests.pages.solutions_page import SolutionsPage
from tests.test_cases.cart_total_price.cart_data_model import CartDataModel

class TestCartTotalPrice:
    def test_cart_total_price(self):
        test_data = TestDataManager.get_single(CartDataModel)

        Logger.info("Step 1: Verify that the cart icon displays 0 items")
        header = NavigationHeader()
        assert header.get_cart_item_count() == test_data.cart_item_count_initial, (
            f"Cart icon count mismatch: expected {test_data.cart_item_count_initial}, "
            f"but got {header.get_cart_item_count()}"
        )

        Logger.info("Step 2: Click on the cart icon and verify that the cart page is opened")
        header.wait_and_click_cart_icon()

        BrowserServices.Instance.browser.refresh()
                
        cart = CartPage()
        assert cart.state.wait_for_displayed, "Cart page is not displayed after opening it"
        
        Logger.info("Step 3: Verify that the empty cart message is displayed")

        empty_cart_message = cart.wait_and_get_empty_basket_message_text()
        assert test_data.cart_is_empty_message in empty_cart_message, (
            f"Empty cart message mismatch: expected to contain "
            f"'{test_data.cart_is_empty_message}', but got '{empty_cart_message}'"
        )

        Logger.info("Step 4: Click 'Go to catalog' and verify navigation to the Solutions page")

        cart.wait_and_click_to_catalog_button()
        solutions_page = SolutionsPage()
        assert solutions_page.state.wait_for_displayed, (
            "Solutions page is not displayed after clicking 'Go to catalog'"
        )

        Logger.info("Step 5: Select product group and add a product with the specified quantity to the cart")

        solutions_page.wait_and_click_product_group_by_name(test_data.product_group_name)

        product_group_page = ProductGroupPage()
        product_group_page.wait_and_click_product_card_by_name(test_data.product_name)

        product_page = ProductPage()
        product_page.wait_and_set_product_amount_to(test_data.amount_of_product)
        product_page.wait_and_click_add_to_cart_button()

        header = NavigationHeader()
        header.wait_for_cart_make_order_popup()
        assert header.get_cart_item_count() == test_data.cart_item_count_after_adding, (
            f"Cart icon count mismatch: expected {test_data.cart_item_count_after_adding}, "
            f"but got {header.get_cart_item_count()}"
        )
        Logger.info("Step 6: Open the cart page")

        header.wait_and_click_cart_icon()
        cart = CartPage()
        assert cart.state.wait_for_displayed, "Cart page not displayed"

        Logger.info("Step 7: Verify product details in the cart (name and quantity)")

        item = cart.get_items_in_cart()[0]
        soft_assert.equal(
            item.name, 
            test_data.product_name, 
            f"Product name mismatch: expected '{test_data.product_name}', but got '{item.name}'"
        )
        soft_assert.equal(
            item.amount, 
            test_data.amount_of_product, 
            f"Product quantity mismatch: expected {test_data.amount_of_product}, but got {item.amount}"
        )

        Logger.info("Step 8: Verify item total price and overall cart total price")

        soft_assert.equal(
            item.total_price, 
            (item.price_for_single_item*item.amount),
            f"Item total price mismatch: expected {item.price_for_single_item * item.amount}, "
            f"but got {item.total_price}"
        )
        assert cart.get_total_price_of_all_items_in_cart() == item.total_price, (
            f"Cart total price mismatch: expected {item.total_price}, "
            f"but got {cart.get_total_price_of_all_items_in_cart()}"
        )
        
        Logger.info("Step 9: Clear the cart and verify that it is empty")

        cart.wait_and_click_remove_all_items_button()
        assert cart.wait_and_get_empty_basket_message_text(), (
            "Cart is not empty after clicking 'Clear cart'"
        )
