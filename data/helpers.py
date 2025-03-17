import string
import random

def generate_email():
    """Генерация случайного email."""
    domains = ["example.com", "test.com", "demo.com"]
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_password(length=12):
    """Генерация случайного пароля."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def generate_name():
    """Генерация случайного имени из букв и цифр (от 8 до 12 символов)."""
    length = random.randint(8, 12)  # Случайная длина от 8 до 12 символов
    characters = string.ascii_letters + string.digits  # Буквы и цифры
    return ''.join(random.choices(characters, k=length))