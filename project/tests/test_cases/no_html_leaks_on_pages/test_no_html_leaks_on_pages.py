import pytest_check as SoftAssert
from py_selenium_auto_core.logging.logger import Logger

from tests.pages.cart_page import CartPage
from tests.pages.home_page import HomePage
from tests.pages.navigation_header import NavigationHeader
from tests.pages.projects_page import ProjectsPage
from tests.pages.services_page import ServicesPage
from tests.pages.solutions_page import SolutionsPage
from tests.pages.vivat_solutions_page import VivatSolutionsPage
from src.utils.ui_checks import UIChecks

import pytest_check as SoftAssert
from src.utils.ui_checks import UIChecks

class TestNoHtmlLeaksOnPages:
    def test_no_html_leaks_on_pages(self):

        home_page = HomePage()
        assert home_page.state.is_displayed(), f"{home_page.name} is not displayed"

        Logger.info("Step 1: Check HTML leaks on Home section")

        header = NavigationHeader()
        text = UIChecks.get_visible_page_text()

        for pattern in UIChecks.get_html_leak_patterns():
            SoftAssert.is_false(
                pattern in text,
                f"HTML leak detected on Home page: {pattern}"
            )

        Logger.info("Step 2: Navigate to VIVAT-IQ Solutions page and check HTML leaks")

        header.wait_and_click_vivat_solutions_link()
        vivat_solutions_page = VivatSolutionsPage()
        text = UIChecks.get_visible_page_text()

        for pattern in UIChecks.get_html_leak_patterns():
            SoftAssert.is_false(
                pattern in text,
                f"HTML leak detected on Vivat Solutions: {pattern}"
            )

        Logger.info("Step 3: Navigate to 1C Solutions page and check HTML leaks")

        header.wait_and_click_1c_solutions_link()
        solutions_page = SolutionsPage()
        text = UIChecks.get_visible_page_text()

        for pattern in UIChecks.get_html_leak_patterns():
            SoftAssert.is_false(
                pattern in text,
                f"HTML leak detected on Solutions: {pattern}"
            )

        Logger.info("Step 4: Navigate to Cart page and check HTML leaks")

        header.wait_and_click_cart_icon()
        cart = CartPage()
        text = UIChecks.get_visible_page_text()

        for pattern in UIChecks.get_html_leak_patterns():
            SoftAssert.is_false(
                pattern in text,
                f"HTML leak detected on Cart: {pattern}"
            )

        Logger.info("Step 5: Navigate to Projects page and check HTML leaks")

        header.wait_and_click_projects_link()
        projects_page = ProjectsPage()
        text = UIChecks.get_visible_page_text()

        for pattern in UIChecks.get_html_leak_patterns():
            SoftAssert.is_false(
                pattern in text,
                f"HTML leak detected on Projects: {pattern}"
            )

        Logger.info("Step 6: Navigate to Services page and check HTML leaks")

        header.wait_and_click_services_link()
        services_page = ServicesPage()
        text = UIChecks.get_visible_page_text()

        for pattern in UIChecks.get_html_leak_patterns():
            SoftAssert.is_false(
                pattern in text,
                f"HTML leak detected on Services Page: {pattern}"
            )
