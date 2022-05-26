from .base_page import BasePage
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import GoToBasket


class BasketPage(BasePage):
    def sould_not_add_basket(self):
        assert self.sould_be_empty_basket(*GoToBasket.BASKET_PASS), 'the basket is not empty'
        assert self.sould_be_empty_basket_message(*GoToBasket.BASKET_MESSAGE), 'the basket is not empty'

    def sould_be_empty_basket(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def sould_be_empty_basket_message(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


