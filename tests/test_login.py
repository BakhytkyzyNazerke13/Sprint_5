import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import NavigationLocators, LoginLocators, RegistrationLocators

EXISTING_USER_EMAIL = "bakhytkyzy_51@gmail.com"  
EXISTING_USER_PASSWORD = "123456"        
BASE_URL = "https://stellarburgers.education-services.ru"


def test_login_from_main_header(driver):
    """1. Вход по кнопке «Войти в аккаунт» на главной странице"""
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)
    
    driver.find_element(*NavigationLocators.LOGIN_BUTTON_HOME).click()
    wait.until(EC.url_contains("/login"))
    
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    
    # ПРОВЕРКА: кнопка "Личный кабинет" стала видимой
    profile_btn = wait.until(EC.visibility_of_element_located(NavigationLocators.PROFILE_BUTTON_HEADER))
    assert profile_btn.is_displayed(), "Кнопка 'Личный кабинет' не видна после входа!"


def test_login_from_profile_button(driver):
    """2. Вход через кнопку «Личный кабинет» в шапке"""
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)
    
    driver.find_element(*NavigationLocators.PROFILE_BUTTON_HEADER).click()
    wait.until(EC.url_contains("/login"))
    
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    
    profile_btn = wait.until(EC.visibility_of_element_located(NavigationLocators.PROFILE_BUTTON_HEADER))
    assert profile_btn.is_displayed()


def test_login_from_register_page(driver):
    """3. Вход через ссылку «Войти» на странице регистрации"""
    wait = WebDriverWait(driver, 10)
    driver.get(f"{BASE_URL}/register")
    wait.until(EC.url_contains("/register"))
    
    driver.find_element(*RegistrationLocators.LOGIN_LINK).click()
    wait.until(EC.url_contains("/login"))
    
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    
    profile_btn = wait.until(EC.visibility_of_element_located(NavigationLocators.PROFILE_BUTTON_HEADER))
    assert profile_btn.is_displayed()


def test_login_from_forgot_password_page(driver):
    """4. Вход через ссылку «Войти» на странице восстановления пароля"""
    wait = WebDriverWait(driver, 10)
    driver.get(f"{BASE_URL}/forgot-password")
    wait.until(EC.url_contains("/forgot-password"))
    
    driver.find_element(*LoginLocators.LOGIN_LINK_FROM_FORGOT).click()
    wait.until(EC.url_contains("/login"))
    
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    
    profile_btn = wait.until(EC.visibility_of_element_located(NavigationLocators.PROFILE_BUTTON_HEADER))
    assert profile_btn.is_displayed()