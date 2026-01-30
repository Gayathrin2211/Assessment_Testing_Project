

class TemplatePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("file:///C:/Assessment_Testing_Project/html_pages/template.html")

    def do_action(self):
        print("Template actions done")
