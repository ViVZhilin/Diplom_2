import allure
from data.data import ErrorMessages
from data.data import Ingredients
from data.urls import Urls

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized(self, api_client, auth_token):
        # Создание заказа
        order_data = {
            "ingredients": [Ingredients.ingredientId1, Ingredients.ingredientId2, Ingredients.ingredientId3]
        }

        headers = {"Authorization": f"{auth_token}"}  # Используем токен из фикстуры
        response = api_client.post(Urls.ORDERS, data=order_data, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self, api_client):
        order_data = {
            "ingredients": [Ingredients.ingredientId1, Ingredients.ingredientId2, Ingredients.ingredientId3]
        }
        response = api_client.post(Urls.ORDERS, data=order_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, api_client):
        response = api_client.post(Urls.ORDERS, data={})
        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == ErrorMessages.INGREDIENTS_REQUIRED

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(self, api_client, auth_token):
        # Создание заказа с невалидным хешем ингредиента
        order_data = {
            "ingredients": ["invalid"]
        }

        headers = {"Authorization": f"{auth_token}"}  # Используем токен из фикстуры
        response = api_client.post(Urls.ORDERS, data=order_data, headers=headers)
        assert response.status_code == 500