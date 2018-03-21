import pytest
from django.contrib.auth.models import User
from pytest_django.live_server_helper import LiveServer
from selenium.webdriver.common.keys import Keys
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
def test_submit_pie_order(selenium: WebDriver, live_server: LiveServer, admin_user: User):
    selenium.implicitly_wait(1)

    # Admin login.
    selenium.get(live_server.url + '/admin/')
    admin_username_input = selenium.find_element_by_css_selector('input[name=username]')
    admin_username_input.send_keys(admin_user.username)
    admin_password_input = selenium.find_element_by_css_selector('input[name=password]')
    admin_password_input.send_keys('password')
    admin_password_input.send_keys(Keys.RETURN)

    # Admin goes to the pie run section.
    pie_run_link = selenium.find_element_by_link_text('Pie_Run')
    pie_run_link.click()

    # Admin clicks on the link to add a pie run.
    add_link = selenium.find_element_by_class_name('addlink')
    add_link.click()

    # Admin selects today as the date for the new pie run.
    today_link = selenium.find_element_by_link_text('Today')
    today_link.click()

    # Admin adds a pie run.
    save_button = selenium.find_element_by_name('_save')
    save_button.click()

    # TODO: admin adds pies.

    # Admin logs out.
    logout_link = selenium.find_element_by_link_text('Log out')
    logout_link.click()

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
