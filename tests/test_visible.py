import time
from pages.elements_page import ElementPage

def test_visible_btn_sidebar(browser):
    test_visible = ElementPage(browser)

    test_visible.visit()
    # test_visible.btn_sidebar_first.click()
    # time.sleep(3)
    # assert test_visible.btn_sidebar_first_textbox.exist()
    assert test_visible.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    test_not_visible = ElementPage(browser)

    test_not_visible.visit()
    assert test_not_visible.btn_sidebar_first_checkbox.visible()
    test_not_visible.btn_sidebar_first.click()
    time.sleep(2)
    assert not test_not_visible.btn_sidebar_first_checkbox.visible()



