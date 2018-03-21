import pytest
from pytest_django.live_server_helper import LiveServer
from selenium.webdriver.remote.webdriver import WebDriver

SAVE_LINK_NAME = '_save'

ADD_LINK_CLASS = 'addlink'


@pytest.mark.nondestructive
def test_can_load_page(selenium: WebDriver, live_server: LiveServer):
    selenium.get(live_server.url)
    body = selenium.find_element_by_css_selector('body')
    assert body is not None


@pytest.mark.nondestructive
def test_homepage_has_h1_pie_runs(selenium: WebDriver, live_server: LiveServer):
    selenium.get(live_server.url)
    heading = selenium.find_element_by_css_selector('h1')
    assert heading.text == 'Pie Runs'


def fill(selenium: WebDriver, text: str, input_name: str):
    input_element = selenium.find_element_by_name(input_name)
    input_element.send_keys(text)
