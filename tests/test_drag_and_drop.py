import time
from pages.droppable import Droppable
from selenium.webdriver import ActionChains
from components.components import WebElement

def test_drag_and_drop(browser):
    drag_and_drop = Droppable(browser)
    action_chains = ActionChains(browser)
    drag_and_drop.visit()

    assert drag_and_drop.drop.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')

    action_chains.drag_and_drop(
        drag_and_drop.drag.find_element(),
        drag_and_drop.drop.find_element()
    ).perform()
    time.sleep(1)

    assert drag_and_drop.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(1)

    action_chains.drag_and_drop_by_offset(
        drag_and_drop.drag.find_element(),
        -200, 0
    ).perform()




