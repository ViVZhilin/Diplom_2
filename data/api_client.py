# data/api_client.py
import requests
import json
from data.helpers import generate_email, generate_password, generate_name

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, data=None, headers=None):
        if headers is None:
            headers = {}
        if data is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(data)
        return requests.post(f"{self.base_url}{endpoint}", data=data, headers=headers)

    def get(self, endpoint, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", headers=headers)

    def patch(self, endpoint, data=None, headers=None):
        if headers is None:
            headers = {}
        if data is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(data)
        return requests.patch(f"{self.base_url}{endpoint}", data=data, headers=headers)

    def delete(self, endpoint, headers=None):
        """Метод для выполнения DELETE-запросов."""
        if headers is None:
            headers = {}
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers)

    # Используем функции из helpers.py
    generate_email = staticmethod(generate_email)
    generate_password = staticmethod(generate_password)
    generate_name = staticmethod(generate_name)