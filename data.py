class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    ORDER_URL = '/api/v1/orders'
    CREATE_COURIER_URL ='/api/v1/courier'
    LOGIN_URL = '/api/v1/courier/login'
    LIST_ORDER_URL = '/api/v1/orders'

class DataForCourier:
    CREATE_COURIER = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }

class DataForAuth:
    CREATE_ID = {
        "login": "ninja",
        "password": "1234"
}

class DataForOrder:
    CREATE_ORDER_BODY = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
class ErrorMessages:
    INSUFFICIENT_DATA_CREATE_MESSAGE = {'message': 'Недостаточно данных для создания учетной записи'}
    LOGIN_ALREADY_USED_MESSAGE = {'message': 'Этот логин уже используется. Попробуйте другой.'}
    NOT_FOUND_MESSAGE = {'message': 'Учетная запись не найдена'}
    INSUFFICIENT_DATA_LOGIN_MESSAGE = {'message':  'Недостаточно данных для входа'}
