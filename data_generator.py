import random

def generate_random_email():
    base_name = "nazerke_bakhytkyzy_51"
    # Генерируем 3 случайные цифры от 100 до 999
    random_digits = random.randint(100, 999)
    # Собираем итоговый email
    return f"{base_name}_{random_digits}@yandex.kz"

def generate_random_password():
    return "Qwerty123"

