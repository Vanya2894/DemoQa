import time
from pages.alerts import Alerts
from pages.elements_page import ElementPage
from components.components import WebElement


def test_page_alert(browser):
    page_alert = Alerts(browser)

    page_alert.visit()
    assert not page_alert.alert()
    page_alert.alertButton.click()
    time.sleep(2)
    assert page_alert.alert()
    page_alert.alert().accept()


def test_alert_text(browser):
    alert_text = Alerts(browser)

    alert_text.visit()
    alert_text.alertButton.click()
    time.sleep(2)
    assert alert_text.alert().text == 'You clicked a button'
    alert_text.alert().accept()
    assert not alert_text.alert()



def test_comfirm(browser):
    comfirm_alert = Alerts(browser)

    comfirm_alert.visit()
    comfirm_alert.comfirmButton.click()
    time.sleep(2)
    comfirm_alert.alert().dismiss()
    assert comfirm_alert.comfirmResult.get_text() == 'You selected Cancel'

def test_ptomt(browser):
    promt = Alerts(browser)

    promt.visit()
    promt.promtButton.click()
    time.sleep(2)
    promt.alert().send_keys('ivan')
    promt.alert().accept()
    assert promt.promtResults.get_text() == 'You entered ivan'
    time.sleep(2)