
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import pytest


def pytest_addoption(parser):
    parser.addoption("--language", action="store",
                     default=None, help="choose language")


@pytest.fixture()
def browser(request):
    language = request.config.getoption("language")
    if not language:
        raise pytest.UsageError("you must set --language option")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': language})
    b = webdriver.Chrome(options=options)
    yield b
    b.quit()
