
import time
from utils.driver_setup import get_driver
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By

def test_dashboard_positive():
    driver = get_driver()
    page = DashboardPage(driver)
    page.open_page()

    # Positive Assertion
    assert "Dashboard" in driver.title

    driver.quit()


def test_dashboard_negative():
    driver = get_driver()
    page = DashboardPage(driver)
    page.open_page()

    # Negative: element that should NOT exist
    elements = driver.find_elements(By.CLASS_NAME, "wrong-class")
    assert len(elements) == 0
    time.sleep(2)

    driver.quit()
