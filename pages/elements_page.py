from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from components.components import WebElement



class ElementPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.elem = WebElement(driver, locator='.playgound-header > div')
        self.icon_elem = WebElement(driver, locator= '#app > header > a > img')
        self.btn_sidebar_first = WebElement(driver, locator='div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, locator='#item-0 > span')



