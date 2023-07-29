from pages.base_page import BasePage
from pages.elements_page import ElementPage

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.tabl_text_have = ElementPage(driver,locator="rt-td")
        self.no_rows_found = ElementPage(driver, locator= "div.rt-noData")
        self.delite = ElementPage(driver, locator= '[title="Delete"]')


