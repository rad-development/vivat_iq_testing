from py_selenium_auto_core.logging.logger import Logger

from tests.pages.navigation_header import NavigationHeader
from tests.pages.projects_page import ProjectsPage

class TestProjectsPageLoadMore:
    def test_projects_page_load_more(self):
        Logger.info("Step 1: Click the 'Projects' button in the header")
        header = NavigationHeader()
        assert header.state.is_displayed(), "Main navigation header is not displayed"
        header.wait_and_click_projects_link()

        Logger.info("Step 2: Verify that projects are displayed on the 'Projects' page")
        projects_page = ProjectsPage()
        projects_before_loading_more = projects_page.get_projects()
        assert projects_before_loading_more, "No projects are displayed on the projects page"

        Logger.info("Step 3: Click the 'Load More' button to load additional projects")
        projects_page.wait_and_click_load_more_projects_button()
   
        assert projects_page.wait_until_load_more_projects_button_is_invisible(), (
            "'Load More' button is still visible after clicking"
        )

        projects_after_loading_more = projects_page.get_projects()
        assert len(projects_before_loading_more) != len(projects_after_loading_more), (
            f"The number of displayed projects did not change after clicking 'Load More' button "
            f"(before: {len(projects_before_loading_more)}, after: {len(projects_after_loading_more)})"
        )