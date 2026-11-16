# UI Автотесты: Stellar Burgers

## Покрытые сценарии

### Регистрация (tests/test_auth.py)
- Проверка ошибки при вводе некорректного (короткого) пароля.
- Проверка успешной регистрации нового пользователя с уникальными данными.

### Вход в аккаунт (tests/test_login.py)
- Вход через кнопку «Войти в аккаунт» на главной странице.
- Вход через кнопку «Личный кабинет» в шапке сайта.
- Вход по ссылке со страницы регистрации.
- Вход по ссылке со страницы восстановления пароля.

### Навигация и Личный кабинет (tests/test_navigation.py)
- Переход в личный кабинет и проверка корректного отображения.
- Переход из личного кабинета в конструктор (по ссылке «Конструктор» и по логотипу).
- Успешный выход из аккаунта по кнопке «Выход».

### Конструктор (tests/test_constructor.py)
- Проверка отображения раздела «Булки» по умолчанию.
- Проверка корректного переключения между разделами «Булки», «Соусы» и «Начинки».

## Структура проекта

```text
Sprint_5/
├── tests/
│   ├── test_auth.py            # Тесты регистрации
│   ├── test_login.py           # Тесты входа в аккаунт
│   ├── test_navigation.py      # Тесты навигации и выхода
│   └── test_constructor.py     # Тесты переключения вкладок конструктора
├── config.py                   # Конфигурация (базовые URL)
├── test_data.py                # Тестовые данные (email, пароли, имена)
├── conftest.py                 # Фикстуры pytest (инициализация браузера)
├── data_generator.py           # Генератор уникальных тестовых данных
├── locators.py                 # Карта локаторов элементов
├── requirements.txt            # Зависимости проекта
├── .gitignore                  # Исключаемые файлы для git
└── README.md                   # Документация проекта
```

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/BakhytkyzyNazerke13/Sprint_5.git 
cd Sprint_5
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Запуск тестов

```bash
# Запуск всех тестов сразу
python -m pytest tests/ -v -s

# Регистрация (файл tests/test_auth.py)
python -m pytest tests/test_auth.py -v -s

# Вход в аккаунт (файл tests/test_login.py)
python -m pytest tests/test_login.py -v -s

# Навигация и Личный кабинет (файл tests/test_navigation.py)
python -m pytest tests/test_navigation.py -v -s

# Конструктор (файл tests/test_constructor.py)
python -m pytest tests/test_constructor.py -v -s
```
