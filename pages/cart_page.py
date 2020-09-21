from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):

    def should_empty_cart(self):
        assert not self.is_element_present(*CartPageLocators.BASKET_ITEMS), "Корзина не пуста"
        assert self.browser.find_element(*CartPageLocators.CONTENT_INNER).text.find("Ваша корзина пуста") != -1, \
            "Нет текста что корзина пуста"