import allure
from data.data import Data


@allure.feature("Авторизация пользователя")
class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, api_client):
        # Данные для авторизации
        data = {
            "email": Data.client_email,
            "password": Data.client_password
        }
        response = api_client.post("/auth/login", data=data)

        # Проверка ответа
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.json()["success"] is True, "Авторизация не была успешной"
        assert "accessToken" in response.json(), "В ответе отсутствует токен"

    @allure.title("Логин с неверным логином и паролем")
    def test_login_invalid_credentials(self, api_client):
        # Данные с неверными учетными данными
        data = {
            "email": "invalid_data",
            "password": "invalid_data"
        }
        response = api_client.post("/auth/login", data=data)

        # Проверка ответа
        assert response.status_code == 401, f"Ожидался код 401, но получен {response.status_code}"
        assert response.json()["success"] is False, "Ожидалось, что success будет False"
        assert response.json()["message"] == "email or password are incorrect", "Неверное сообщение об ошибке"