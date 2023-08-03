import time
from pages.progress_bar_page import ProgressBar

def test_progress_bar(browser):
    prog_bar = ProgressBar(browser)
    prog_bar.visit()
    time.sleep(2)

    prog_bar.startStopButton.click()
    while True:
        if prog_bar.progressBar.get_dom_attribute('aria-valuenow') == '51':
            prog_bar.startStopButton.click()
            break

