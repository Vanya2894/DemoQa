from pages.base_page import BasePage
from components.components import WebElement



class Alerts(BasePage):
    def __init__(self, driver):
     self.base_url = 'https://demoqa.com/alerts'
     super().__init__(driver, self.base_url)

     self.alertButton = WebElement(driver, locator = '#alertButton')
     self.comfirmButton = WebElement(driver, locator= '#confirmButton')
     self.promtButton = WebElement(driver, locator= '#promtButton')
     self.promtResults = WebElement(driver, locator= '#promptResult')
     self.timerAlertButton = WebElement(driver, locator= '#timerAlertButton')
     self.comfirmResult = WebElement(driver, locator='#confirmResult')



