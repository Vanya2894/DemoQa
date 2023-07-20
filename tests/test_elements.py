from pages.elements_page import ElementPage

def test_finde_elements(browser):
    finde = ElementPage(browser)

    finde.visit()
    assert finde.btns_first_menu.check_count_elements(9)