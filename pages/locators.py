from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name=registration_submit]")

class ProductPageLocators():
    ADD_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.XPATH, "//h1")
    BOOK_PRICE = (By.XPATH, "//p[@class='price_color']")
    BOOK_NAME_IN_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[1]/strong")
    BOOK_PRICE_IN_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[3]/p/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_CART_BUTTON = (By.XPATH, "(//a[contains(@href,'basket')])[1]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    CONTENT_INNER = (By.CSS_SELECTOR, "#content_inner")