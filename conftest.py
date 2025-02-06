import pytest
from selene import browser, be

@pytest.fixture(scope="function")
def open_browser():
    print('Открыл браузер!')
    browser.open('https://duckduckgo.com')
    browser.driver.set_window_size(1700, 1280)
    yield
    print('Закрыл браузер!')
    browser.quit()



