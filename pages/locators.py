from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class GoToBasket:
    GO_TO_BASKET = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    BASKET_PASS = (By.CLASS_NAME, "col-sm-6 h3")
    BASKET_MESSAGE = (By.XPATH, '// *[ @ id = "content_inner"] / p')


class MainPageLocators:
    pass
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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


class RegisterField:
    LOGIN_FIELD = (By.ID, 'id_registration-email')
    PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    DOUBLE_PASSWORD_FIELD = (By.ID, 'id_registration-password2')
    BUTTON_REGISTER = (By.XPATH, '//*[@id="register_form"]/button')
