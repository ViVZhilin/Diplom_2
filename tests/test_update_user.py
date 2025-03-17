import allure
import datetime
from data.urls import Urls
from data.data import ErrorMessages


@allure.feature("Изменение данных пользователя")
class TestUpdateUser:
    @allure.title("Изменение данных с авторизацией")
    def test_update_user_authorized(self, api_client, auth_token):
        # Изменение данных с использованием токена из фикстуры
        current_time = str(datetime.datetime.now().time())
        update_data = {
            "name": current_time
        }
        headers = {"Authorization": auth_token}
        response = api_client.patch(Urls.USER, data=update_data, headers=headers)

        # Проверка ответа
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["name"] == current_time

    @allure.title("Изменение данных без авторизации")
    def test_update_user_unauthorized(self, api_client):
        # Попытка обновления данных без авторизации
        update_data = {
            "name": "Unauthorized Update"
        }
        response = api_client.patch(Urls.USER, data=update_data)

        # Проверка ответа
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == ErrorMessages.UNAUTHORIZED