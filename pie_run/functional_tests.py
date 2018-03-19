import pytest


# def setup_module(module):
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PyPie.settings")
#     execute_from_command_line(['/Users/stefano/dev/PyPie/manage.py', 'runserver', '8000'])


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
