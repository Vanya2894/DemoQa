from pages.demoqa import DemoQa
from pages.elements_page import ElementPage
def test_go_to_page_elements (browser):
    page = DemoQa (browser)
    elements_page = ElementPage(browser)

    page.visit()
    assert page.equa_url()
    page.btn_elements.click()
    assert elements_page.equa_url()


