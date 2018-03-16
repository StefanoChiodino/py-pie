from unittest import TestCase

from django.core.management.commands import runserver
from selenium import webdriver


class WebdriverTestCase(TestCase):
    def setUp(self):
        runserver.run('127.0.0.1', 8000, runserver.get_internal_wsgi_application())
        self.url = 'http://127.0.0.1:8000/'
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
