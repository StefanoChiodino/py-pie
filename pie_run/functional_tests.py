import pytest
from pytest_django.live_server_helper import LiveServer
from selenium.webdriver.remote.webdriver import WebDriver


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


@pytest.mark.django_db
def test_submit_pie_order(selenium: WebDriver, live_server: LiveServer):
    selenium.implicitly_wait(1)
    selenium.get(live_server.url)
    pie_run_link = selenium.find_element_by_css_selector('li a')
    pie_run_link.click()

    name_input = selenium.find_element_by_css_selector('input[name=client_name]')
    client_name = 'test name'
    name_input.send_keys(client_name)

    pie_inputs = selenium.find_elements_by_class_name('pie-input')
    for pie_input in pie_inputs:
        pie_input.send_keys('1')

    submit = selenium.find_element_by_css_selector('input[type=submit]')
    submit.click()

    heading = selenium.find_element_by_css_selector('h1')
    assert heading.text == 'Pie Run Order'

    body = selenium.find_element_by_css_selector('body')
    assert client_name in body.text
