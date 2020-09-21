import math

from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException

from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_in_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART_BUTTON).click()

    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_name_book_in_cart(self, book_name):
        assert book_name == self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE).text, "Имя не совпадает в сообщении"

    def should_be_price_book_in_cart(self, book_price):
        assert book_price == self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MESSAGE).text, "Цена не совпадает в сообщении"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе представлено, но не должно быть"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Успешное сообщение не исчезло"
