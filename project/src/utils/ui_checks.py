from py_selenium_auto.browsers.browser_services import BrowserServices
from selenium.webdriver.common.by import By


class UIChecks:
    @staticmethod
    def get_visible_page_text():
        return BrowserServices.Instance.browser.driver.find_element(By.TAG_NAME, "body").text

    @staticmethod
    def get_html_leak_patterns():
        return [
            "<div",
            "<p",
            "<h1",
            "<span",
            "<a",
            "&lt;div",
            "&lt;p",
            "&lt;a",
            "style=",
            "onmouseover=",
            "onmouseout="
        ]