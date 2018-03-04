from unittest import TestCase

from selenium import webdriver


class FunctionalTestDetails(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_load_page(self):
        self.browser.get('http://127.0.0.1:8000/')
        body = self.browser.find_element_by_css_selector('body')
        self.assertNotEqual(body, None)
