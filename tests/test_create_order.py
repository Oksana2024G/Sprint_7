import requests
import allure
import pytest
from data import Url

class TestCreateOrder:

    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GRAY'],
        []
    ])
    @allure.title('Создание заказа')
    def test_create_order(self, color):

        payload = {
            "firstName": "Александр",
            "lastName": "Пушкин",
            "address": "Лукоморье,  д.25",
            "metroStation": 25,
            "phone": "+79998887766",
            "rentTime": 3,
            "deliveryDate": "2025-01-30",
            "comment": "Позови золотую рыбку",
            "color": color
        }

        r = requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=payload)
        assert r.status_code == 201
        assert 'track' in r.json()
