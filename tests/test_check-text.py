from pages.elements_page import ElementPage
from components.components import WebElement

def test_page_elements(browser):
    page_text = ElementPage(browser)
    page_text.visit()
    assert page_text.elem.get_text() == 'Elements'
    assert page_text.icon_elem.exist()
    assert page_text.btn_sidebar_first.exist()
    assert page_text.btn_sidebar_first_textbox.exist()

