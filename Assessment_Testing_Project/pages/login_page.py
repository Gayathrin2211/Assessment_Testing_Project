from selenium.webdriver.common.by import By
from utils.config import EMAIL, PASSWORD, URL

class LoginPage:
    def _init_(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get(URL)
        self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, "//button").click()
