
import time
from utils.driver_setup import get_driver
from pages.test_module_page import TestModulePage

def test_test_module_positive():
    driver = get_driver()
    page = TestModulePage(driver)
    page.open_page()

    assert "Test Module" in driver.title
    driver.quit()


def test_test_module_negative():
    driver = get_driver()
    page = TestModulePage(driver)
    page.open_page()

    assert "Random Page" not in driver.title
    time.sleep(2)
    driver.quit()
