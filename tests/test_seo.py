from pages.demoqa import DemoQa

def test_soe(browser):
    demo_qa_title = DemoQa(browser)

    demo_qa_title.visit()
    assert demo_qa_title.get_title() == 'DEMOQA'

