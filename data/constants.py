from helpers.data_for_create_courier import GenerateData


class Constants:
    base_url_page = 'https://qa-scooter.praktikum-services.ru'

    path_create_courier = '/api/v1/courier'
    path_login_courier = '/api/v1/courier/login'
    path_create_order = '/api/v1/orders'
    path_get_list_order = '/api/v1/orders?courierId='
    PATH_DELETE_COURIER = '/api/v1/courier/:id'

    duplicate_data_for_create_courier = {"login": "olegShadrikov", "password": "1234567890", "firstName": "saske"}
    not_login_for_creating_courier = {"password": f'{GenerateData.generate_random_string(10)}', "firstName": f'{GenerateData.generate_random_string(10)}'}
    not_password_for_creating_courier = {"login": f'{GenerateData.generate_random_string(10)}', "firstName": f'{GenerateData.generate_random_string(10)}'}
    data_with_all_required_parameters = {"login": f'{GenerateData.generate_random_string(10)}', "password": f'{GenerateData.generate_random_string(10)}'}
    data_duplicate_login_for_create_courier = {"login": "ninja", "password": f'{GenerateData.generate_random_string(10)}', "firstName": f'{GenerateData.generate_random_string(10)}'}
    successful_test_response = '{"ok":true}'

    data_for_authorization = {"login": "olegShadrikov", "password": "1234567890"}
    data_for_authorization_without_password = {"login": "olegShadrikov"}
    data_for_authorization_without_login = {"password": "1234567890"}

    message_missing_parameters = "Недостаточно данных для входа"
    message_account_not_found = "Учетная запись не найдена"
    message_create_courier_duplicate_login = "Этот логин уже используется"
    message_create_courier_insufficient_data = "Недостаточно данных для создания учетной записи"

    id_successful_authorization = 451536
    id_order = 407533

    orders = [{
            "id": 407533,
            "courierId": 451536,
            "firstName": "Дмитрий",
            "lastName": "Шадриков",
            "address": "Ульяновс321к, 142 apt.",
            "metroStation": "4",
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06T00:00:00.000Z",
            "track": 336288,
            "color": [
                "GREY"
            ],
            "comment": "Saske, come back ауыto Ульяновск",
            "createdAt": "2025-01-20T10:37:17.752Z",
            "updatedAt": "2025-01-20T10:40:29.832Z",
            "status": 1
        },
        {
            "id": 407539,
            "courierId": 451536,
            "firstName": "Дмитрий",
            "lastName": "Шадриков",
            "address": "Ульяновс321к, 142 apt.",
            "metroStation": "4",
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06T00:00:00.000Z",
            "track": 336288,
            "color": [
                "GREY"
            ],
            "comment": "Saske, come back ауыto Ульяновск",
            "createdAt": "2025-01-20T10:40:29.847Z",
            "updatedAt": "2025-01-20T10:40:29.847Z",
            "status": 1
        }]