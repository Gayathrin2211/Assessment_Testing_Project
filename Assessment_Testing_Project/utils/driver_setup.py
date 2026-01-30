'''from selenium import webdriver

def get_driver():
    driver = webdriver.Chrome() 
    driver.maximize_window()
    return driver
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    return driver
