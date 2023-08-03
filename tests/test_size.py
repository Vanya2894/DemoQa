import time
from pages.demoqa import DemoQa
from pages.elements_page import ElementPage

def test_size(browser):
    size = DemoQa(browser)

    size.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000,1000)

def test_visible_nav_bar(browser):
    nav_bar = ElementPage(browser)

    nav_bar.visit()
    browser.set_window_size(400, 565)
    assert nav_bar.nav_bar.visible()
    browser.set_window_size(1000,1000)
    time.sleep(1)
    assert not nav_bar.nav_bar.visible()
