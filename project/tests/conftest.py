import logging
import os
import pytest

from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.logging.logger import Logger

from src.utils.config_manager import ConfigManager


@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    work_dir = RootPathHelper.current_root_path(__file__)
    os.chdir(work_dir)
    Logger.info(f'Setting work_dir: {work_dir}')
    for log_name in ["selenium.webdriver.remote.remote_connection",
                     "selenium.webdriver.common.selenium_manager",
                     "urllib3.connectionpool"]:
        logging.getLogger(log_name).disabled = True
    Logger.info("Environment ready")
    yield

@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    base_url = ConfigManager.get_config().base_url

    BrowserServices.Instance.browser.maximize()
    BrowserServices.Instance.browser.go_to(base_url)
    BrowserServices.Instance.browser.wait_for_page_to_load()

    yield

    if BrowserServices.Instance.is_browser_started:
        Logger.info("Closing browser")
        BrowserServices.Instance.browser.quit()
