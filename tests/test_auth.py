import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import NavigationLocators, LoginLocators, RegistrationLocators
from data_generator import generate_random_email, generate_random_password

from config import BASE_URL
from test_data import USER_NAME, SHORT_PASSWORD


class TestAuth:
    """Тесты регистрации"""

    def test_successful_registration(self, driver):
        """Тест проверяет успешную регистрацию нового пользователя"""
        wait = WebDriverWait(driver, 10)
        
        # 1. Открываем главную страницу
        driver.get(BASE_URL)
        
        # 2. Переходим на страницу входа
        driver.find_element(*NavigationLocators.LOGIN_BUTTON_HOME).click()
        wait.until(EC.url_contains("/login"))
        
        # 3. Переходим на страницу регистрации
        driver.find_element(*LoginLocators.REGISTER_LINK).click()
        wait.until(EC.url_contains("/register"))
        
        # 4. Ждем появления полей формы
        wait.until(EC.presence_of_element_located(RegistrationLocators.EMAIL_INPUT))
        
        # 5. Генерируем данные + берем имя из test_data
        test_name = USER_NAME
        test_email = generate_random_email()
        test_password = generate_random_password() 
        
        # 6. Заполняем форму
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(test_name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(test_password)
        
        # 7. Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()
        
        # 8. ОЖИДАНИЕ: ждем, пока URL изменится на /login
        wait.until(EC.url_contains("/login"))
        
        # 9. ПРОВЕРКА
        assert "/login" in driver.current_url


    def test_registration_with_short_password(self, driver):
        """Тест проверяет, что при коротком пароле появляется ошибка"""
        wait = WebDriverWait(driver, 10)
        
        # 1. Открываем главную страницу и переходим к регистрации
        driver.get(BASE_URL)
        driver.find_element(*NavigationLocators.LOGIN_BUTTON_HOME).click()
        wait.until(EC.url_contains("/login"))
        
        driver.find_element(*LoginLocators.REGISTER_LINK).click()
        wait.until(EC.url_contains("/register"))
        wait.until(EC.presence_of_element_located(RegistrationLocators.EMAIL_INPUT))
        
        # 2. Заполняем форму, используя данные из test_data
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(USER_NAME)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(generate_random_email())
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(SHORT_PASSWORD)  # Короткий пароль из test_data!
        
        # 3. Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()
        
        # 4. ПРОВЕРКА: ждем появления текста ошибки и проверяем его
        error_message = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR_MESSAGE)
        )
        
        assert error_message.text == "Некорректный пароль", \
            f"Ожидали 'Некорректный пароль', но получили: '{error_message.text}'"
        
        # 5. Проверка: должны остаться на странице регистрации
        assert "/register" in driver.current_url