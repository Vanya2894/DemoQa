from pages.base_page import BasePage
from components.components import WebElement
class ProgressBar(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super(). __init__ (driver, self.base_url)


        self.startStopButton = WebElement(driver, locator='#startStopButton')
        self.progressBar = WebElement(driver, locator='#progressBar > div')




