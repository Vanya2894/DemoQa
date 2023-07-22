import time
from pages.text_box_page import TextBox
def test_clear(browser):
    clear_plase = TextBox(browser)

    clear_plase.visit()
    clear_plase.full_name.send_keys('testetssupertester')
    time.sleep(2)
    clear_plase.full_name.clear()
    time.sleep(2)
    assert clear_plase.full_name.get_text() == ''

