import allure

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized(self, api_client, auth_token):
        # Создание заказа
        order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa77", "61c0c5a71d1f82001bdaaa6d"]
        }

        headers = {"Authorization": f"{auth_token}"}  # Используем токен из фикстуры
        response = api_client.post("/orders", data=order_data, headers=headers)
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.json()["success"] is True, "Заказ не был успешно создан"
        assert "order" in response.json(), "В ответе отсутствует поле 'order'"

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self, api_client):
        order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa77", "61c0c5a71d1f82001bdaaa6d"]
        }
        response = api_client.post("/orders", data=order_data)
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.json()["success"] is True, "Заказ не был успешно создан"

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, api_client):
        response = api_client.post("/orders", data={})
        assert response.status_code == 400, f"Ожидался код 400, но получен {response.status_code}"
        assert response.json()["success"] is False, "Ожидалось, что success будет False"
        assert response.json()["message"] == "Ingredient ids must be provided", "Неверное сообщение об ошибке"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(self, api_client, auth_token):
        # Создание заказа с невалидным хешем ингредиента
        order_data = {
            "ingredients": ["invalid"]
        }

        headers = {"Authorization": f"{auth_token}"}  # Используем токен из фикстуры
        response = api_client.post("/orders", data=order_data, headers=headers)
        assert response.status_code == 500, f"Ожидался код 500, но получен {response.status_code}"