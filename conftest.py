import pytest
from data.api_client import ApiClient
from data.data import Data
from data.urls import Urls


@pytest.fixture
def api_client():
    return ApiClient(base_url=Urls.BASE_URL)


@pytest.fixture
def auth_token(api_client):
    # Логин для получения токена
    login_data = {
        "email": Data.client_email,
        "password": Data.client_password
    }
    login_response = api_client.post(Urls.LOGIN, data=login_data)
    if login_response.status_code != 200:
        raise Exception("Ошибка авторизации")
    return login_response.json()["accessToken"]


@pytest.fixture
def create_and_delete_user(api_client):
    # Создание пользователя
    user_data = {
        "email": ApiClient.generate_email(),
        "password": ApiClient.generate_password(),
        "name": ApiClient.generate_name()
    }
    response = api_client.post(Urls.REGISTER, data=user_data)
    if response.status_code != 200:
        raise Exception("Ошибка при создании пользователя")

    # Получаем токен для удаления пользователя
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    login_response = api_client.post(Urls.LOGIN, data=login_data)
    if login_response.status_code != 200:
        raise Exception("Ошибка при авторизации нового пользователя")
    token = login_response.json()["accessToken"]

    yield user_data  # Передаем данные пользователя в тест

    # Удаление пользователя после завершения теста
    headers = {"Authorization": token}
    api_client.delete(Urls.USER, headers=headers)