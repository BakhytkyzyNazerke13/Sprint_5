import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import NavigationLocators, LoginLocators, RegistrationLocators

# Импортируем конфигурацию и тестовые данные
from config import BASE_URL
from test_data import VALID_EMAIL, VALID_PASSWORD


class TestLogin:
    """Тесты входа в аккаунт"""

    def test_login_from_main_header(self, driver):
        """1. Вход по кнопке «Войти в аккаунт» на главной странице"""
        wait = WebDriverWait(driver, 10)
        driver.get(BASE_URL)
        
        driver.find_element(*NavigationLocators.LOGIN_BUTTON_HOME).click()
        wait.until(EC.url_contains("/login"))
        
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        
        # ПРОВЕРКА: ждём кнопку "Оформить заказ" (появляется только после входа)
        order_button = wait.until(EC.visibility_of_element_located(NavigationLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не видна после входа!"


    def test_login_from_profile_button(self, driver):
        """2. Вход через кнопку «Личный кабинет» в шапке"""
        wait = WebDriverWait(driver, 10)
        driver.get(BASE_URL)
        
        driver.find_element(*NavigationLocators.PROFILE_BUTTON_HEADER).click()
        wait.until(EC.url_contains("/login"))
        
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        
        order_button = wait.until(EC.visibility_of_element_located(NavigationLocators.ORDER_BUTTON))
        assert order_button.is_displayed()


    def test_login_from_register_page(self, driver):
        """3. Вход через ссылку «Войти» на странице регистрации"""
        wait = WebDriverWait(driver, 10)
        driver.get(f"{BASE_URL}/register")
        wait.until(EC.url_contains("/register"))
        
        driver.find_element(*RegistrationLocators.LOGIN_LINK).click()
        wait.until(EC.url_contains("/login"))
        
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        
        order_button = wait.until(EC.visibility_of_element_located(NavigationLocators.ORDER_BUTTON))
        assert order_button.is_displayed()


    def test_login_from_forgot_password_page(self, driver):
        """4. Вход через ссылку «Войти» на странице восстановления пароля"""
        wait = WebDriverWait(driver, 10)
        driver.get(f"{BASE_URL}/forgot-password")
        wait.until(EC.url_contains("/forgot-password"))
        
        driver.find_element(*LoginLocators.LOGIN_LINK_FROM_FORGOT).click()
        wait.until(EC.url_contains("/login"))
        
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        
        order_button = wait.until(EC.visibility_of_element_located(NavigationLocators.ORDER_BUTTON))
        assert order_button.is_displayed()