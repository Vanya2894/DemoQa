from pages.elements_page import ElementPage
from pages.checkbox_page import CheckBox
from components.components import WebElement
def test_finde_elements(browser):
    finde = ElementPage(browser)

    finde.visit()
    assert finde.btns_first_menu.check_count_elements(9)


def test_count_checkbox(browser):
    count_checkbox = CheckBox(browser)

    count_checkbox.visit()
    assert count_checkbox.check_box_btn.check_count_elements(1)
    count_checkbox.btn_plus_checkbox.click()
    assert count_checkbox.check_box_btn.check_count_elements(17)
    for element in count_checkbox.check_box_btn.finde_elements():
        assert element.is_displayed()

    count_checkbox.refresh()
    assert count_checkbox.check_box_btn.check_count_elements(1)


