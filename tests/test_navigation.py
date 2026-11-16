import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import NavigationLocators, LoginLocators, ProfileLocators

# Импортируем конфигурацию и тестовые данные вместо хардкода
from config import BASE_URL
from test_data import VALID_EMAIL, VALID_PASSWORD


def _login_and_go_to_main(driver, wait):
    """Вспомогательная функция для входа в аккаунт"""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    
    wait.until(EC.visibility_of_element_located(NavigationLocators.ORDER_BUTTON))


class TestNavigation:
    """Тесты навигации и управления сессией"""

    def test_go_to_profile_from_header(self, driver):
        """1. Переход в личный кабинет по клику на «Личный кабинет» в шапке"""
        wait = WebDriverWait(driver, 10)
        
        # 1. Сначала входим в аккаунт
        _login_and_go_to_main(driver, wait)
        
        # 2. Кликаем на "Личный Кабинет" в шапке
        driver.find_element(*NavigationLocators.PROFILE_BUTTON_HEADER).click()
        
        # 3. ПРОВЕРКА: ждем и убеждаемся, что попали именно на /account/profile
        wait.until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url


    def test_go_to_constructor_from_profile_via_menu(self, driver):
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


    def test_go_to_constructor_from_profile_via_logo(self, driver):
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


    def test_logout_from_profile(self, driver):
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