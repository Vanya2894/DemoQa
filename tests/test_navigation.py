from pages.demoqa import DemoQa
from pages.elements_page import ElementPage

def test_navigation(browser):
    navigation = DemoQa(browser)
    elements_page = ElementPage(browser)

    navigation.visit()
    navigation.btn_elements.click()


    elements_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elements_page.equa_url()
