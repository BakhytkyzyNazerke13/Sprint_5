import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import NavigationLocators, LoginLocators, ProfileLocators

EXISTING_USER_EMAIL = "bakhytkyzy_51@gmail.com"  
EXISTING_USER_PASSWORD = "123456"        
BASE_URL = "https://stellarburgers.education-services.ru"


def _login_and_go_to_main(driver, wait):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    
    wait.until(EC.visibility_of_element_located(NavigationLocators.PROFILE_BUTTON_HEADER))


def test_go_to_profile_from_header(driver):
    """1. Переход в личный кабинет по клику на «Личный кабинет» в шапке"""
    wait = WebDriverWait(driver, 10)
    
    # 1. Сначала входим в аккаунт (оказываемся на главной с кнопкой "Личный кабинет")
    _login_and_go_to_main(driver, wait)
    
    # 2. Кликаем на "Личный Кабинет" в шапке
    driver.find_element(*NavigationLocators.PROFILE_BUTTON_HEADER).click()
    
    # 3. ПРОВЕРКА: ждем и убеждаемся, что попали именно на /account/profile
    wait.until(EC.url_contains("/account/profile"))
    assert "/account/profile" in driver.current_url


def test_go_to_constructor_from_profile_via_menu(driver):
    """2. Переход из ЛК в конструктор по клику на «Конструктор»"""
    wait = WebDriverWait(driver, 10)
    
    _login_and_go_to_main(driver, wait)
    
    # 1. Переходим в профиль 
    driver.find_element(*NavigationLocators.PROFILE_BUTTON_HEADER).click()
    wait.until(EC.url_contains("/account/profile"))
    
    # 2. Кликаем на "Конструктор" в шапке
    driver.find_element(*NavigationLocators.CONSTRUCTOR_LINK).click()
    
    # 3. ПРОВЕРКА: ждем и убеждаемся, что вернулись на главную страницу (/)
    wait.until(lambda d: d.current_url == BASE_URL + "/")
    assert driver.current_url == BASE_URL + "/"


def test_go_to_constructor_from_profile_via_logo(driver):
    """3. Переход из ЛК в конструктор по клику на логотип"""
    wait = WebDriverWait(driver, 10)
    
    _login_and_go_to_main(driver, wait)
    
    profile_btn = wait.until(EC.element_to_be_clickable(NavigationLocators.PROFILE_BUTTON_HEADER))
    profile_btn.click()
    
    # Ждем изменения URL
    wait.until(EC.url_contains("/account/profile"))
    assert "/account/profile" in driver.current_url
    
    # 2. Кликаем на логотип
    logo = wait.until(EC.element_to_be_clickable(NavigationLocators.LOGO_LINK))
    logo.click()
    
    # 3. ПРОВЕРКА: ждем и убеждаемся, что вернулись на главную страницу (/)
    wait.until(lambda d: d.current_url == BASE_URL + "/")
    assert driver.current_url == BASE_URL + "/"


def test_logout_from_profile(driver):
    """4. Выход из аккаунта по кнопке «Выход»"""
    wait = WebDriverWait(driver, 10)
    
    _login_and_go_to_main(driver, wait)
    
    # 1. Переходим в профиль, чтобы там была кнопка "Выход"
    driver.find_element(*NavigationLocators.PROFILE_BUTTON_HEADER).click()
    wait.until(EC.url_contains("/account/profile"))
    
    # 2. Нажимаем кнопку "Выход"
    driver.find_element(*ProfileLocators.LOGOUT_BUTTON).click()
    
    # 3. ПРОВЕРКА: перекидывает на страницу /login
    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url