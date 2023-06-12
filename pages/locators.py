from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    GOOD_TITLE = (By.CSS_SELECTOR, 'div.product_main>h1')
    GOOD_TITLE_IN_CART = (By.CSS_SELECTOR, 'div.alertinner > strong')

    GOOG_PRICE = (By.CSS_SELECTOR, 'div.product_main>p.price_color')
    CART_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    MSG_SUCCESS_ADDED = (By.XPATH, '//*[@id="messages"]/div[1]/div')
