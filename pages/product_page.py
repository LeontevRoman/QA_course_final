from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        button_ad_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_CARDS)
        button_ad_to_basket.click()

    def title_book_in_cards(self):
        title_book = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        title_book_basket = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_BASKET).text
        assert title_book_basket == title_book, 'Sorry book not basket add'

    def price_book_in_cards(self):
        title_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        title_price_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        assert title_price == title_price_basket, 'Sorry price not true'

