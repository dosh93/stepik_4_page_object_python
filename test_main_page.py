import time

def test_view_button_add_cart(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    assert browser.find_element_by_css_selector('.btn-add-to-basket').is_displayed(), "Нет кнопки добавить в корзину"