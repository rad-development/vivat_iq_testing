import pytest_check as SoftAssert
from py_selenium_auto_core.logging.logger import Logger

from tests.pages.navigation_header import NavigationHeader
from tests.pages.vivat_solutions_page import VivatSolutionsPage


class TestVivatSolutionsSorting:
    def test_vivat_solutions_sorting(self):
        Logger.info("Step 1: Click the 'VIVAT-IQ Solutions' button in the header")

        header = NavigationHeader()
        assert header.state.is_displayed(), "Main navigation header is not displayed"
        header.wait_and_click_vivat_solutions_link()

        Logger.info("Step 2: Verify the list of solutions on the 'VIVAT-IQ Solutions' page")

        vivat_solutions_page = VivatSolutionsPage()
        assert vivat_solutions_page.state.is_displayed(), "'VIVAT-IQ Solutions' page did not open"

        list_of_stuff = vivat_solutions_page.get_vivat_iq_solutions_titles()
        for stuff in list_of_stuff:
            Logger.debug(f"{stuff}")

        Logger.info("Step 3: Select sorting by price (lowest first)")

        vivat_solutions_page.sort_by_price_ascending()
        prices_ascending = vivat_solutions_page.get_all_prices()

        SoftAssert.equal(
            prices_ascending,
            sorted(prices_ascending),
            f"Prices are not sorted in ascending order: {prices_ascending}"
        )

        Logger.info("Step 4: Select sorting by price (highest first)")

        vivat_solutions_page.sort_by_price_descending()
        prices_descending = vivat_solutions_page.get_all_prices()

        SoftAssert.equal(
            prices_descending,
            sorted(prices_descending, reverse=True),
            f"Prices are not sorted in descending order: {prices_descending}"
        )