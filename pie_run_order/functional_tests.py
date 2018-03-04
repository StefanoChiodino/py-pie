from WebdriverTestCase import WebdriverTestCase


class FunctionalTestDetails(WebdriverTestCase):
    def test_can_load_page(self):
        self.browser.get(self.url)
        body = self.browser.find_element_by_css_selector('body')
        self.assertNotEqual(body, None)
