import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import locators

def test_elements_sber_main_page():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()

    driver.find_element(By.ID, "main-page")

    driver.find_element(By.TAG_NAME, "span")

    driver.find_element(By.CSS_SELECTOR, "#main-page > div")

    driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']/following::div[1]")

    driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']/following::div[1]/a[1]")

    driver.find_element(By.XPATH, "//a[text()=\"СберБанк Онлайн\"]/parent::div[1]")

    driver.find_element(By.XPATH, "//a[text()='Курсы валют']/parent::div[1]")
    driver.find_element(By.XPATH, "(//a[text()='Офисы'])[1]")

    # sber_online_button = driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    # sber_online_button.click()

    geo_button = driver.find_element(By.XPATH, "//a[@title='Изменить регион']")
    geo_button.click()

    region_name_field = driver.find_element(By.XPATH, "//input[@aria-label='Введите имя региона']")
    region_name_field.send_keys("Какая-то область")
    time.sleep(3)
    region_name_field.clear()
    region_name_field.send_keys("Ростовская область")

    region_name_button = driver.find_element(By.XPATH, "//button[text()='Ростовская область']")
    region_name_button.click()

    time.sleep(3)
