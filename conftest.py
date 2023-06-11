import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language: en ot ru')

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'init.accept_language': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print('\nQuit browser...')
    browser.quit()