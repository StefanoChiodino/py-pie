import pytest
from django.contrib.auth.models import User
from pytest_django.live_server_helper import LiveServer
from selenium.webdriver.remote.webdriver import WebDriver

from pie_run.functional_tests import fill, ADD_LINK_CLASS, SAVE_LINK_NAME


@pytest.mark.django_db
def test_submit_pie_order(selenium: WebDriver, live_server: LiveServer, admin_user: User):
    selenium.implicitly_wait(1)

    # Admin login.
    selenium.get(live_server.url + '/admin/')
    fill(selenium, admin_user.username, 'username')
    fill(selenium, 'password', 'password')
    selenium.find_element_by_css_selector('input[type=submit]').click()

    # Admin goes to the pie run section
    selenium.find_element_by_link_text('Pie_Run').click()

    # Admin clicks on the link to add a pie run.
    selenium.find_element_by_class_name(ADD_LINK_CLASS).click()

    # Admin selects today as the date for the new pie run.
    selenium.find_element_by_link_text('Today').click()

    # Admin adds a pie run.
    selenium.find_element_by_name(SAVE_LINK_NAME).click()

    # Admin goes to the pie section.
    selenium.find_element_by_link_text('Pie Runner Admin').click()
    selenium.find_element_by_link_text('Pie').click()

    # Admin clicks on the link to add a pie.
    selenium.find_element_by_class_name(ADD_LINK_CLASS).click()

    # Admin fills in Pie form.
    pie_name = 'pie name'
    fill(selenium, pie_name, 'name')
    fill(selenium, '1', 'price')

    # Admin saves the pie.
    selenium.find_element_by_name(SAVE_LINK_NAME).click()

    # Admin logs out.
    selenium.find_element_by_link_text('Log out').click()

    selenium.get(live_server.url)
    selenium.find_element_by_css_selector('li a').click()

    client_name = 'test name'
    fill(selenium, client_name, 'client_name')

    pie_inputs = selenium.find_elements_by_class_name('pie-input')
    for pie_input in pie_inputs:
        pie_input.send_keys('1')

    submit = selenium.find_element_by_css_selector('input[type=submit]')
    submit.click()

    heading = selenium.find_element_by_css_selector('h1')
    assert heading.text == 'Pie Run Order'

    body = selenium.find_element_by_css_selector('body')
    assert client_name in body.text
    assert pie_name in body.text
