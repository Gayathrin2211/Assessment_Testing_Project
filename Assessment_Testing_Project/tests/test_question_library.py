import time
from utils.driver_setup import get_driver
from pages.question_library_page import QuestionLibraryPage

def test_question_library_positive():
    driver = get_driver()
    page = QuestionLibraryPage(driver)
    page.open_page()

    assert "Question Library" in driver.title
    driver.quit()


def test_question_library_negative():
    driver = get_driver()
    page = QuestionLibraryPage(driver)
    page.open_page()

    assert "Fake Page" not in driver.title
    time.sleep(2)
    driver.quit()
