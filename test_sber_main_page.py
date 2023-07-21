import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.main_page import MainPage
from pages import locators
import Steps.support_steps as support_steps


# Тесты проверяют переход по ссылкам в меню
def test_moving_menu_links(browser):
    main_page = MainPage(browser, "http://www.sberbank.ru/")
    # Открываем тестовую страницу
    main_page.open()
    # Убедимся, что ссылка с курсами валют присутствует
    main_page.should_be_exchange_rates_link()
    # Находим ссылку курсов валют и нажимаем на неё
    main_page.click_on_exchange_rates_link()
    # Проверяем, что мы на нужной странице
    main_page.assert_exchange_rates_title()


def test_check_geo_position(browser):
    # Выставляем ожидание в 10 секунд
    browser.implicitly_wait(10)
    # Открываем тестовую страницу
    browser.get("http://www.sberbank.ru/")
    # Разворачиваем окно на весь экран
    browser.maximize_window()

    geo_button = browser.find_element(By.XPATH, "//a[@title='Изменить регион']")
    geo_button.click()

    region_name_field = browser.find_element(By.XPATH, "//input[@aria-label='Введите имя региона']")
    region_name_field.send_keys("Ростовская область")
    region_name_button = browser.find_element(By.XPATH, "//button[text()='Ростовская область']")
    region_name_button.click()

    geo_button = browser.find_element(By.XPATH, "//a[@title='Изменить регион']")
    assert geo_button.text == "Ростовская область"

    time.sleep(3)


def test_incorrect_geo_position(browser):
    try:
        # Выставляем ожидание в 10 секунд
        browser.implicitly_wait(10)
        # Открываем тестовую страницу
        browser.get("http://www.sberbank.ru/")
        # Разворачиваем окно на весь экран
        browser.maximize_window()

        geo_button = browser.find_element(By.XPATH, locators.GEOPOSITION_LINK)
        geo_button.click()

        region_name_field = browser.find_element(By.XPATH, locators.REGION_NAME_FIELD)
        region_name_field.send_keys(support_steps.generate_random_string(5))
        time.sleep(3)
    finally:
        browser.quit()


def test_count_links(browser):
    # Выставляем ожидание в 10 секунд
    browser.implicitly_wait(10)
    # Открываем тестовую страницу
    browser.get("http://www.sberbank.ru/")
    # Разворачиваем окно на весь экран
    browser.maximize_window()

    browser.find_element(By.XPATH, "//a[text()='Курсы валют']")
    assert len("Курсы валют") != 4

    time.sleep(3)


def test_color_link(browser):
    # Выставляем ожидание в 10 секунд
    browser.implicitly_wait(10)
    # Открываем тестовую страницу
    browser.get("http://www.sberbank.ru/")
    # Разворачиваем окно на весь экран
    browser.maximize_window()

    sber_online_button = browser.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    color_before_perform = sber_online_button.value_of_css_property('color')
    ActionChains(browser).move_to_element(sber_online_button).perform()
    color_after_perform = sber_online_button.value_of_css_property('color')

    assert color_before_perform != color_after_perform
    time.sleep(3)
