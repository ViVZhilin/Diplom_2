import allure
import datetime
from data.data import Data


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
        response = api_client.patch("/auth/user", data=update_data, headers=headers)

        # Проверка ответа
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.json()["success"] is True, "Обновление данных не было успешным"
        assert response.json()["user"]["name"] == current_time, "Имя пользователя не обновилось"

    @allure.title("Изменение данных без авторизации")
    def test_update_user_unauthorized(self, api_client):
        # Попытка обновления данных без авторизации
        update_data = {
            "name": "Unauthorized Update"
        }
        response = api_client.patch("/auth/user", data=update_data)

        # Проверка ответа
        assert response.status_code == 401, f"Ожидался код 401, но получен {response.status_code}"
        assert response.json()["success"] is False, "Ожидалось, что success будет False"
        assert response.json()["message"] == "You should be authorised", "Неверное сообщение об ошибке"