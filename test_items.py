import time

def test_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(5)
    button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "Should be a buttton"