from py_selenium_auto_core.logging.logger import Logger

from tests.pages.navigation_header import NavigationHeader
from tests.pages.solutions_page import SolutionsPage
from tests.pages.product_group_page import ProductGroupPage
from tests.pages.product_page import ProductPage

class TestSolutionsPage:
    def test_solutions_page(self):
        Logger.info("Step 1: Click the '1C Solutions' button in the header")

        header = NavigationHeader()
        assert header.state.is_displayed(), "Main navigation header is not displayed"
        header.wait_and_click_1c_solutions_link()

        Logger.info("Step 2: Verify the list of solutions on the '1C Solutions' page")
        solutions_1c_page = SolutionsPage()
        assert solutions_1c_page.state.is_displayed(), "'1C Solutions' page did not open"

        solutions_1c_titles = solutions_1c_page.get_1c_solutions()
        assert solutions_1c_titles, "The list of solutions on the page is empty"

        name_from_1c_solutions_page = solutions_1c_titles[0].lower()

        Logger.info("Step 3: Click the first solution card, and vrify the product group name")
        solutions_1c_page.wait_and_click_first_1c_solution_card()

        product_group_page = ProductGroupPage()
        name_from_1c_product_group_page = product_group_page.get_product_group_name().lower()
        assert name_from_1c_solutions_page == name_from_1c_product_group_page, (
            f"name of the product group displayed on the page of 1C Solutions: {name_from_1c_solutions_page}"
            f"does not match the name displayed on its page: {name_from_1c_product_group_page}")
        
        Logger.info("Step 4: Verify the list of products in the group is not empty")
        product_names = product_group_page.get_product_names()
        assert product_names, "The list of products in the group is empty"
        name_of_product_from_product_group_page = product_names[0].lower()

        Logger.info("Step 5: Click the first product card")
        product_group_page.wait_and_click_first_product_card()

        Logger.info("Step 6: Verify the product name")
        product_page = ProductPage()
        name_of_product_from_product_page = product_page.get_product_name().lower()
        assert name_of_product_from_product_group_page == name_of_product_from_product_page, (
            f"Product name '{name_of_product_from_product_page}' "
            f"does not match the name from the product group '{name_of_product_from_product_group_page}'"
        )

