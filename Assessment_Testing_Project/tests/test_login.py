from utils.driver_setup import get_driver
from pages.login_page import LoginPage

def test_login():
    driver = get_driver()
    LoginPage(driver).login()
    assert "dashboard" in driver.current_url
    driver.quit()
