from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_exchange_rates_link(self):
        assert self.is_element_present(*MainPageLocators.EXCHANGE_RATES_LINK), "Ссылка 'Курсы валют' отсутствует"

    def click_on_exchange_rates_link(self):
        button = self.driver.find_element(*MainPageLocators.EXCHANGE_RATES_LINK)
        button.click()

    def assert_exchange_rates_title(self):
        assert self.driver.find_element(
            *MainPageLocators.FIRST_TITLE_ON_PAGE).text == "Курсы валют", "Первый заголовок не Курсы валют"
