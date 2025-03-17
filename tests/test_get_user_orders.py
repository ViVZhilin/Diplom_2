import allure
from data.data import ErrorMessages
from data.urls import Urls

@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_authorized(self, api_client, auth_token):
        # Получение заказов с использованием токена из фикстуры
        headers = {"Authorization": auth_token}
        response = api_client.get(Urls.ORDERS, headers=headers)

        # Проверка ответа
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "orders" in response.json()

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_unauthorized(self, api_client):
        # Получение заказов без авторизации
        response = api_client.get(Urls.ORDERS)

        # Проверка ответа
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == ErrorMessages.UNAUTHORIZED