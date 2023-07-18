from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement
class DemoQa(BasePage):

     def __init__(self, driver):
         self.base_url = 'https://demoqa.com/'
         super().__init__(driver, self.base_url)
         self.icon = WebElement(driver,locator='#app > header > a')
         self.btn_elements = WebElement(driver,locator='#app > div > div > div.home-body > div > div:nth-child(1)')



     # def exist_icon(sellf):
     #    try:
     #       sellf.icon.find_element()
     #    except NoSuchElementException:
     #       return False
     #    return True


    # # def clic_on_the_icon(self):
    #      return self.find_element(locator='#app > header > a').click()
    #
    #
    #  #def clic_on_the_btn_elements (self):
    #      return self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()


