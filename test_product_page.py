import time
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
#    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()

    page.should_be_button_add_to_cart()
    page.user_can_add_good_to_cart()

    page.should_be_good_title_same_as_in_cart()
    page.shold_be_correct_cart_price()
    page.should_be_correct_msg_about_good_name()
