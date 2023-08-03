import time
import pytest
from pages.base_page import BasePage
from pages.demoqa import DemoQa
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab


@pytest.mark.parametrize('pages', [Alerts, DemoQa, BrowserTab])
def test_seo_meta(browser, pages):
    page_seo = pages(browser)

    page_seo.visit()
    time.sleep(2)
    assert page_seo.metaViev.exist()
    assert page_seo.metaViev.get_dom_attribute('name') == 'viewport'
    assert page_seo.metaViev.get_dom_attribute('content') == 'width=device-width,initial-scale=1'