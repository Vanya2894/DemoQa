# Не прошел
import allure
from pages.text_box_page import TextBox

@allure.feature('check attr') # "проверка арибута"
@allure.story('Проверка отсутствия атрибута')#"проверка отсуствия атрибута"
@allure.severity(allure.severity_level.BLOCKER) # "степень серьезности проверки"
def test_placeholder(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    assert text_box_page.full_name.get_dom_attribute('plaseholder') == 'Full Name'

@allure.feature('check attr')
@allure.story('Проверка упавшего теста')
@allure.severity(allure.severity_level.BLOCKER)
def test_fail():
    assert 111 == 222

