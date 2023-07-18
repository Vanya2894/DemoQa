from pages.demoqa import DemoQa
def test_icon_exist(browser):
    demoqa_page = DemoQa(browser)
    demoqa_page.visit()
    demoqa_page.icon.click()
    assert demoqa_page.equa_url()
    assert demoqa_page.icon.exist()




#     browser.get('https://demoqa.com/')
#     icon =  browser.find_element(By.CSS_SELECTOR, '#app > header > a')
#
#     if icon is None:
#         print('Элемент не найден')
#     else:
#        print("Элемент найден")

