import time
from utils.driver_setup import get_driver
from pages.template_page import TemplatePage

def test_template_positive():
    driver = get_driver()
    page = TemplatePage(driver)
    page.open_page()

    assert "Template" in driver.title
    driver.quit()


def test_template_negative():
    driver = get_driver()
    page = TemplatePage(driver)
    page.open_page()

    assert "Wrong Title" not in driver.title
    time.sleep(2)
    driver.quit()
