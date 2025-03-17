import allure
from data.data import ErrorMessages
from data.urls import Urls

@allure.feature("Создание пользователя")
class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, api_client):
        data = {
            "email": api_client.generate_email(),
            "password": api_client.generate_password(),
            "name": api_client.generate_name()
        }
        response = api_client.post(Urls.REGISTER, data=data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user(self, api_client):
        data = {
            "email": "existing_user@example.com",
            "password": "password123",
            "name": "Existing User"
        }
        # Первый запрос (успешная регистрация)
        api_client.post(Urls.REGISTER, data=data)
        # Второй запрос (пользователь уже существует)
        response = api_client.post(Urls.REGISTER, data=data)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == ErrorMessages.USER_ALREADY_EXISTS

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_missing_field(self, api_client):
        data = {
            "email": api_client.generate_email(),
            "password": api_client.generate_password()
        }
        response = api_client.post(Urls.REGISTER, data=data)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == ErrorMessages.REQUIRED_FIELDS