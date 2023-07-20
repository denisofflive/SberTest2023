import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import locators


def test_moving_menu_links():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()

        exchange_rates_button = driver.find_element(By.XPATH, locators.EXCHANGE_RATES_LINK)
        exchange_rates_button.click()

        first_page_title = driver.find_element(By.XPATH, locators.FIRST_TITLE_ON_PAGE)
        assert first_page_title.text == "Курсы валют"
        time.sleep(3)
    finally:
        # Закрываем браузер
        driver.quit()



def test_check_geo_position():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    geo_button = driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    geo_button.click()

    region_name_field = driver.find_element(By.XPATH, "//input[@aria-label='Введите имя региона']")
    region_name_field.send_keys("Ростовская область")
    region_name_button = driver.find_element(By.XPATH, "//button[text()='Ростовская область']")
    region_name_button.click()

    geo_button = driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    assert geo_button.text == "Ростовская область"

    time.sleep(3)


def test_count_links():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//a[text()='Курсы валют']")
    assert len("Курсы валют") != 4

    time.sleep(3)


def test_color_link():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    sber_online_button = driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    color_before_perform = sber_online_button.value_of_css_property('color')
    ActionChains(driver).move_to_element(sber_online_button).perform()
    color_after_perform = sber_online_button.value_of_css_property('color')

    assert color_before_perform != color_after_perform
    time.sleep(3)


