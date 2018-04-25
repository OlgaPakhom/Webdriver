from selenium import webdriver
import pytest

@pytest.fixture(scope='session')
def browser():
    ch = webdriver.Chrome()
    yield ch # <<<<< Where testing occur!
    ch.close()

@pytest.fixture(scope='function', autouse=True)    
def wiki_open(browser):
    browser.get('http://wikipedia.org')
    
langs = ['Українська', 'English', 'Deutsch', 'Polska', 'Italiano']

@pytest.mark.parametrize('language', langs)
def test_language_on_main_page(language, browser):
    assert language in browser.find_element_by_tag_name('body').text

    
lcodes = ['de', 'en', 'uk', 'pl']
   
@pytest.mark.parametrize('language', lcodes)
def test_language_pages_on_main_page(browser, language):
    lang_locators = [f'#js-link-box-{language} > strong']
    browser.find_element_by_css_selector(lang_locators).click()
    assert 'Wiki' in browser.title
     