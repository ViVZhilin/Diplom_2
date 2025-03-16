import string
import random
import requests
import json  # Импортируем модуль json для сериализации данных

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, data=None, headers=None):
        if headers is None:
            headers = {}
        # Если данные передаются, устанавливаем заголовок Content-Type
        if data is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(data)  # Сериализуем данные в JSON-строку
        return requests.post(f"{self.base_url}{endpoint}", data=data, headers=headers)

    def get(self, endpoint, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", headers=headers)

    def patch(self, endpoint, data=None, headers=None):
        if headers is None:
            headers = {}
        # Если данные передаются, устанавливаем заголовок Content-Type
        if data is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(data)  # Сериализуем данные в JSON-строку
        return requests.patch(f"{self.base_url}{endpoint}", data=data, headers=headers)

    @staticmethod
    def generate_email():
        """Генерация случайного email."""
        domains = ["example.com", "test.com", "demo.com"]
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(domains)
        return f"{username}@{domain}"

    @staticmethod
    def generate_password(length=12):
        """Генерация случайного пароля."""
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))

    @staticmethod
    def generate_name():
        """Генерация случайного имени из букв и цифр (от 8 до 12 символов)."""
        length = random.randint(8, 12)  # Случайная длина от 8 до 12 символов
        characters = string.ascii_letters + string.digits  # Буквы и цифры
        return ''.join(random.choices(characters, k=length))