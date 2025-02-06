from selene import browser, be, have

# Сделал поиск на duckduckgo, т.к. не пройти капчу в google

def test_succesfull_google(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python - GitHub'))

def test_succesfull_duckduckgo_fail(open_browser):
    browser.element('[name="q"]').should(be.blank).type('sfvedbfgbfnfnfynyrfnyntyntyntyntyntynt').press_enter()
    browser.element('html').should(have.text('результаты не найдены.'))