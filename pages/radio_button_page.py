from pages.base_page import BasePage
from components.components import WebElement

class RadioButton(BasePage):

        def __init__(self, driver):
            self.base_url = 'https://demoqa.com/radio-button'
            super().__init__(driver, self.base_url)

            self.rafio_yes = WebElement(driver, locator='#yesRadio')
            self.radio_impressive = WebElement(driver, locator='#impressiveRadio')
            self.radio_selected = WebElement(driver, locator='mt-3')
            self.radio_no = WebElement(driver, locator= 'custom-control-label disabled')
