class BasePage():
    def __init__(self, driver, base_url="https://www.wonderwe.com/"):
        self.driver = driver
        self.base_url = base_url

    def navigate(self, base_url):
        self.driver.get(base_url)

