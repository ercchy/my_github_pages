class SiteTest(LiveServerTestCase):
    def setup(self):
        self.browser = webdriver.Firefox()