import pytest


# def setup_module(module):
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PyPie.settings")
#     execute_from_command_line(['/Users/stefano/dev/PyPie/manage.py', 'runserver', '8000'])
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.mark.nondestructive
def test_can_load_page(selenium, url: str):
    selenium.get(url)
    body = selenium.find_element_by_css_selector('body')
    assert body is not None


@pytest.mark.nondestructive
def test_homepage_has_h1_pie_runs(selenium, url: str):
    selenium.get(url)
    heading = selenium.find_element_by_css_selector('h1')
    assert heading.text == 'Pie Runs'


@pytest.mark.nondestructive
def test_submit_pie_order(selenium: WebDriver, url: str):
    selenium.implicitly_wait(1)
    selenium.get(url)
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
