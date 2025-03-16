import pytest
from data.api_client import ApiClient
from data.data import Data

@pytest.fixture
def api_client():
    return ApiClient(base_url="https://stellarburgers.nomoreparties.site/api")

@pytest.fixture
def auth_token(api_client):
    # Логин для получения токена
    login_data = {
        "email": Data.client_email,
        "password": Data.client_password
    }
    login_response = api_client.post("/auth/login", data=login_data)
    assert login_response.status_code == 200, "Ошибка авторизации"
    return login_response.json()["accessToken"]