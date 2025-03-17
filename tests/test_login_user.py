import allure
from data.data import Data
from data.data import ErrorMessages
from data.urls import Urls

@allure.feature("Авторизация пользователя")
class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, api_client):
        # Данные для авторизации
        data = {
            "email": Data.client_email,
            "password": Data.client_password
        }
        response = api_client.post(Urls.LOGIN, data=data)

        # Проверка ответа
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным логином и паролем")
    def test_login_invalid_credentials(self, api_client):
        # Данные с неверными учетными данными
        data = {
            "email": "invalid_data",
            "password": "invalid_data"
        }
        response = api_client.post(Urls.LOGIN, data=data)

        # Проверка ответа
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == ErrorMessages.INCORRECT_CREDENTIALS