from selenium.webdriver.common.by import By

class NavigationLocators:
    """Локаторы для шапки сайта и общей навигации"""
    
    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_BUTTON_HOME = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
    # Кнопка «Личный кабинет» в шапке сайта
    PROFILE_BUTTON_HEADER = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    
    # Логотип Stellar Burgers
    LOGO_LINK = (By.CSS_SELECTOR, "div[class*='header__logo'] a")
    
    # Ссылка «Конструктор» в шапки сайта
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    # Кнопка "Оформить заказ" (появляется только после успешного входа)
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")


class RegistrationLocators:
    """Локаторы для страницы регистрации (/register)"""
    
    # Поле ввода имени на форме регистрации
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    
    # Поле ввода email на форме регистрации
    EMAIL_INPUT = (By.XPATH, "//label[contains(., 'Email')]/following-sibling::input")
    
    # Поле ввода пароля на форме регистрации
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    
    # Кнопка «Зарегистрироваться» на форме регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    
    # Ссылка «Войти» под формой регистрации
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    
    # Текст ошибки при вводе некорректного (слишком короткого) пароля
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")


class LoginLocators:
    """Локаторы для страницы входа (/login)"""
    
    # Поле ввода email на форме входа
    EMAIL_INPUT = (By.XPATH, "//label[contains(., 'Email')]/following-sibling::input")
    
    # Поле ввода пароля на форме входа
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    
    # Кнопка «Войти» на форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    # Ссылка «Восстановить пароль» под формой входа
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    
    # Ссылка «Войти» на странице восстановления пароля
    LOGIN_LINK_FROM_FORGOT = (By.CSS_SELECTOR, "a[href='/login']")
    
    # Ссылка «Зарегистрироваться» на странице входа
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")


class ConstructorLocators:
    """Локаторы для раздела «Конструктор» на главной странице"""
    
    # Вкладка «Булки» в меню конструктора
    BUNS_TAB = (By.XPATH, "//span[contains(text(), 'Булки')]")
    
    # Вкладка «Соусы» в меню конструктора
    SAUCES_TAB = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    
    # Вкладка «Начинки» в меню конструктора
    FILLINGS_TAB = (By.XPATH, "//span[contains(text(), 'Начинки')]")
    
    # Заголовок раздела «Булки» (используется для проверки скролла страницы)
    BUNS_HEADER = (By.XPATH, "//h2[contains(text(), 'Булки')]")
    
    # Заголовок раздела «Соусы» (используется для проверки скролла страницы)
    SAUCES_HEADER = (By.XPATH, "//h2[contains(text(), 'Соусы')]")
    
    # Заголовок раздела «Начинки» (используется для проверки скролла страницы)
    FILLINGS_HEADER = (By.XPATH, "//h2[contains(text(), 'Начинки')]")


class ProfileLocators:
    """Локаторы для страницы профиля (/account/profile)"""
    
    # Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")