import time
import pytest
from pages.demoqa import DemoQa
from pages.alerts import Alert
from pages.browser_tab import BrowserTab

def test_soe(browser):
    demo_qa_title = DemoQa(browser)

    demo_qa_title.visit()
    assert demo_qa_title.get_title() == 'DEMOQA'

@pytest.mark.parametrize('pages', [Alerts, DemoQa, BrowserTab])#Accordion (у меня отсуствует)
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'



