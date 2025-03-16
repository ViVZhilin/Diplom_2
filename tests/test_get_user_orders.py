import allure
from data.data import Data


@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_authorized(self, api_client, auth_token):
        # Получение заказов с использованием токена из фикстуры
        headers = {"Authorization": auth_token}
        response = api_client.get("/orders", headers=headers)

        # Проверка ответа
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.json()["success"] is True, "Запрос не был успешным"
        assert "orders" in response.json(), "В ответе отсутствует поле 'orders'"

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_unauthorized(self, api_client):
        # Получение заказов без авторизации
        response = api_client.get("/orders")

        # Проверка ответа
        assert response.status_code == 401, f"Ожидался код 401, но получен {response.status_code}"
        assert response.json()["success"] is False, "Ожидалось, что success будет False"
        assert response.json()["message"] == "You should be authorised", "Неверное сообщение об ошибке"