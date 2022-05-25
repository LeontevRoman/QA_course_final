from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_CARDS = (By.CLASS_NAME, 'btn-add-to-basket')
    BOOK_TITLE = (By.TAG_NAME, 'h1')
    BOOK_TITLE_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    BOOK_PRICE_BASKET = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")
