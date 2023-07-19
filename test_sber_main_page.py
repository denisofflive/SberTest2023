import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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

    sber_online_button = driver.find_element(By.XPATH, "//a[text()='СберБанк Онлайн']")
    sber_online_button.click()

    time.sleep(3)







