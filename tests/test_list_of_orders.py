import requests
import allure
import pytest
from data import Url

class TestGetListOrders:


    @allure.title('Получение списка заказов')
    def test_get_list_of_orders(self):

        payload = {
            "firstName": "Александр",
            "lastName": "Пушкин",
            "address": "Лукоморье,  д.25",
            "metroStation": 25,
            "phone": "+79998887766",
            "rentTime": 3,
            "deliveryDate": "2025-01-30",
            "comment": "Позови золотую рыбку",
            "color": [
        "BLACK"
    ]
        }

        requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=payload)
        list_orders = requests.get(f'{Url.BASE_URL}{Url.LIST_ORDER_URL}')
        assert list_orders.status_code == 200
        assert "orders" in list_orders.json()
