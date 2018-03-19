import pytest


@pytest.fixture(scope='session', autouse=True, name='domain')
def get_domain() -> str:
    """ The domain where the website is hosted. """
    return '127.0.0.1'


@pytest.fixture(scope='session', autouse=True, name='port')
def get_port() -> int:
    """ The port where the website is hosted. """
    return 8000


@pytest.fixture(scope='session', autouse=True, name='url')
def get_url(domain: str, port: int) -> str:
    """ The url where there website is hosted. """
    return f'http://{domain}:{port}/'
