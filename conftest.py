import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    # 1. Создаем драйвер перед каждым тестом
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # 2. Передаем управление тесту
    yield driver

    time.sleep(3)
    # 3. Закрываем браузер после завершения теста (автономность!)
    driver.quit()