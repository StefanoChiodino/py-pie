from unittest import TestCase

from selenium import webdriver


class WebdriverTestCase(TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/'
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
