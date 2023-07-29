import pytest
from pages.demoqa import DemoQa
from components.components import WebElement
from pages.radio_button_page import RadioButton

@pytest.mark.skip
def test_decor(browser):
    demoqa_decor = DemoQa(browser)
    demoqa_decor.visit()

    assert demoqa_decor.decor.check_count_elements(6)

    for element in demoqa_decor.decor.find_elements():
        assert not element.text == ''


def test_decor_2(browser):
    decor_2 = RadioButton(browser)

    if decor_2.code_staus() != 200:
        pytest.skip(reason=f'страница {decor_2.base_url} недоступна')

    decor_2.visit()

    decor_2.rafio_yes.click_force()
    assert decor_2.radio_selected.get_text() == 'You have selected Yes'

    decor_2.radio_impressive.click_force()
    assert decor_2.radio_selected.get_text() == 'You have selected Impressive'

    assert 'disabled' in decor_2.radio_no.get_dom_attribute('class')