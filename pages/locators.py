from selenium.webdriver.common.by import By


class BasePageLocators:

    FIRST_TITLE_ON_PAGE = (By.XPATH, "(//h1)[1]")


class MainPageLocators(BasePageLocators):

    EXCHANGE_RATES_LINK = (By.XPATH, "//a[text()='Курсы валют']")
    GEOPOSITION_LINK = (By.XPATH, "//a[@title='Изменить регион']")
    REGION_NAME_FIELD = (By.XPATH, "//input[@aria-label='Введите имя региона']")
    ROSTOV_REGION_FILED = (By.XPATH, "//button[text()='Ростовская область']")
    SBER_ONLINE_LINK = (By.XPATH, "//a[text()='СберБанк Онлайн']")
