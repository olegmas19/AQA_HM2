import pytest
from selene import browser, be

@pytest.fixture(scope="session")
def open_browser():
    print('Открыл браузер!')
    browser.open('https://duckduckgo.com')
    browser.driver.set_window_size(1700, 1280)
    yield
    print('Закрыл браузер!')
    browser.quit()

@pytest.fixture(scope="session")
def clear_search():
    search_input = browser.element('[name="q"]')
    if search_input.should(be.not_.blank):
        search_input.clear()



