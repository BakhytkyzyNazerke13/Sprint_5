import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConstructorLocators

BASE_URL = "https://stellarburgers.education-services.ru/"

def test_buns_section_opened_by_default(driver):
    """Проверка, что при открытии сайта по умолчанию активен раздел «Булки»"""
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)
    
    # Ждем, пока на экране появится заголовок "Булки" (признак того, что раздел активен)
    wait.until(EC.visibility_of_element_located(ConstructorLocators.BUNS_HEADER))
    assert True  # Если заголовок появился, значит раздел "Булки" открыт по умолчанию

def test_switch_from_buns_to_sauces(driver):
    """1. Переход с вкладки 'Булки' на 'Соусы'"""
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)
    
    # Кликаем на вкладку "Соусы"
    wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)).click()
    
    # ПРОВЕРКА: ждем, пока на экране не появится заголовок "Соусы"
    wait.until(EC.visibility_of_element_located(ConstructorLocators.SAUCES_HEADER))
    assert True  # Если мы дошли до этой строки, значит заголовок появился


def test_switch_from_sauces_to_fillings(driver):
    """2. Переход с вкладки 'Соусы' на 'Начинки'"""
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)
    
    # Сначала переходим на "Соусы"
    wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)).click()
    wait.until(EC.visibility_of_element_located(ConstructorLocators.SAUCES_HEADER))
    
    # Затем кликаем на "Начинки"
    wait.until(EC.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB)).click()
    
    # ПРОВЕРКА: ждем, пока на экране не появится заголовок "Начинки"
    wait.until(EC.visibility_of_element_located(ConstructorLocators.FILLINGS_HEADER))
    assert True


def test_switch_from_fillings_to_buns(driver):
    """3. Переход с вкладки 'Начинки' на 'Булки'"""
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)
    
    # Сначала переходим на "Начинки"
    wait.until(EC.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB)).click()
    wait.until(EC.visibility_of_element_located(ConstructorLocators.FILLINGS_HEADER))
    
    # Затем кликаем обратно на "Булки"
    wait.until(EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB)).click()
    
    # ПРОВЕРКА: ждем, пока на экране не появится заголовок "Булки"
    wait.until(EC.visibility_of_element_located(ConstructorLocators.BUNS_HEADER))
    assert True