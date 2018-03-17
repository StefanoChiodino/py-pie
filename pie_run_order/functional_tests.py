import pytest


@pytest.fixture
def domain() -> str:
    return '127.0.0.1'


@pytest.fixture
def port() -> int:
    return 8000


@pytest.fixture
def url(domain: str, port: int) -> str:
    return f'http://{domain}:{port}/'


# def setup_module(module):
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PyPie.settings")
# execute_from_command_line(['/Users/stefano/dev/PyPie/manage.py', 'runserver', '8000'])


def test_can_load_page(selenium, url: str):
    selenium.get(url)
    body = selenium.find_element_by_css_selector('body')
    assert body is not None
