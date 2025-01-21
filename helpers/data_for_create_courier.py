import random
import string

import requests


class GenerateData:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def create_data():
        login = GenerateData.generate_random_string(10)
        password = GenerateData.generate_random_string(10)
        first_name = GenerateData.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

    @staticmethod
    def crate_data_for_create_order(color):
        data_for_create_order = {
            "firstName": GenerateData.generate_random_string(10),
            "lastName": GenerateData.generate_random_string(10),
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }

    @staticmethod
    def delete_courier(data):
        response = requests.post(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={'login': data['login'], 'password': data['password']})
        a = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{response.json()['id']}')