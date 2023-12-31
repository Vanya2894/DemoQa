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
        self.btn_sidebar_first_textbox = WebElement(driver, locator=' div:nth-child(1) > div > ul>#item-0')
        self.btn_sidebar_first_checkbox = WebElement(driver, locator='div:nth-child(1) > div > ul>#item-1')
        self.btns_first_menu = WebElement(driver, locator='div:nth-child(1) > div > ul > li')
        self.nav_bar = WebElement(driver, locator='div > nav')



