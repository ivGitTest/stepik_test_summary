from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), 'No button to add the good to cart'

    def should_be_good_price(self):
        assert self.is_element_present(*ProductPageLocators.GOOG_PRICE), 'No good price is found'

    def user_can_add_good_to_cart(self):
        btn = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        btn.click()
        self.solve_quiz_and_get_code() #, 'Can\'t get quize code'

    def should_be_good_title_same_as_in_cart(self):
        global good_title
        good_title = self.browser.find_element(*ProductPageLocators.GOOD_TITLE).text
        good_title_in_cart = self.browser.find_element(*ProductPageLocators.GOOD_TITLE_IN_CART).text
        assert good_title == good_title_in_cart, 'Good\'s title is not same as good name in the cart'

    def shold_be_correct_cart_price(self):
        good_price = self.browser.find_element(*ProductPageLocators.GOOG_PRICE).text.partition('\xa3')[2]
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text.partition('\xa3')[2]
        assert cart_price == good_price, 'Cart price is not equal product price'

    def should_be_correct_msg_about_good_add(self):
        #expected_msg = "has been added to your basket."
        expected_msg = " был добавлен в вашу корзину."
        site_msg = self.browser.find_element(*ProductPageLocators.MSG_SUCCESS_ADDED).text
        #print('expected_msg: ', expected_msg)
        #print('site_msg: ', site_msg)
        assert expected_msg in site_msg, 'Success message is not found'
