from py_selenium_auto_core.logging.logger import Logger

from tests.pages.navigation_header import NavigationHeader
from tests.pages.services_page import ServicesPage
from tests.pages.service_page import ServicePage

class TestServicesPageNavigation:
    def test_services_page_navigation(self):
        Logger.info("Step 1: Click the 'Services' button in the header")
        header = NavigationHeader()
        assert header.state.is_displayed(), "Main navigation header is not displayed"
        header.wait_and_click_services_link()

        Logger.info("Step 2: Verify the list of services on the 'Services' page")
        services_page = ServicesPage()
        service_titles = services_page.get_services()
        assert service_titles, "The list of services on the page is empty"

        name_from_services_page = service_titles[0].lower()

        Logger.info("Step 3: Click the first service link")
        services_page.wait_and_click_first_service_link()

        Logger.info("Step 4: Compare the service name from the list with the name on the service page")
        service_page = ServicePage()
        name_from_specific_service_page = service_page.get_service_name_from_breadcrumbs()
        assert name_from_services_page == name_from_specific_service_page, (
            f"Service name '{name_from_services_page}' from the list "
            f"does not match the name on the service page '{name_from_specific_service_page}'"
        )
