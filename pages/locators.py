from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.XPATH, "//h1")
    BOOK_PRICE = (By.XPATH, "//p[@class='price_color']")
    BOOK_NAME_IN_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[1]/strong")
    BOOK_PRICE_IN_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[3]/p/strong")