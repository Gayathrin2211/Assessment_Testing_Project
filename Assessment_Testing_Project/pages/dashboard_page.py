
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("file:///C:/Assessment_Testing_Project/html_pages/dashboard.html")

    def do_action(self):
        print("Dashboard actions done")
