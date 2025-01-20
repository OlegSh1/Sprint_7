from http.client import responses

import pytest
import requests
from data.constants import Constants
from helpers.data_for_create_courier import GenerateData


class TestCreateCourier:
    def test_create_courier_correct_value_successful_creation(self):
        response = requests.post(f"{Constants.base_url_page}{Constants.path_create_courier}", data=GenerateData.create_data())
        assert response.status_code == 201 and response.json()['ok'] == True

    def test_create_courier_duplicate_data_unsuccessful_creation(self):
        response = requests.post(f"{Constants.base_url_page}{Constants.path_create_courier}", data=Constants.duplicate_data_for_create_courier)
        assert response.status_code == 409 and response.json()['message'] == Constants.message_create_courier_duplicate_login

    @pytest.mark.parametrize('data_for_create, code, response_body, key',
    [
        [Constants.data_with_all_required_parameters, 201, True, 'ok'],
        [Constants.not_login_for_creating_courier, 400, Constants.message_create_courier_insufficient_data, 'message']
    ])
    def test_create_courier_requires_all_mandatory_fields(self, data_for_create, code, response_body, key):
        response = requests.post(f"{Constants.base_url_page}{Constants.path_create_courier}", data=data_for_create)
        assert response.status_code == code and response.json()[key] == response_body

    @pytest.mark.parametrize('data_for_create, code, response_body, key',
    [
        [GenerateData.create_data(), 201, True, 'ok'],
        [Constants.duplicate_data_for_create_courier, 409, Constants.message_create_courier_duplicate_login, 'message'],
        [Constants.not_login_for_creating_courier, 400, Constants.message_create_courier_insufficient_data, 'message']
    ])
    def test_return_response_code_correct_code(self, data_for_create, code, response_body, key):
        response = requests.post(f"{Constants.base_url_page}{Constants.path_create_courier}", data=data_for_create)
        assert response.status_code == code and response.json()[key] == response_body

    def test_successful_test_returned_true(self):
        response = requests.post(f"{Constants.base_url_page}{Constants.path_create_courier}", data=GenerateData.create_data())
        assert response.text == Constants.successful_test_response and response.status_code == 201

    @pytest.mark.parametrize('data_for_create,code, response_body',
    [
        [Constants.not_password_for_creating_courier, 400, Constants.message_create_courier_insufficient_data],
        [Constants.not_login_for_creating_courier, 400, Constants.message_create_courier_insufficient_data]
    ])
    def test_error_returned_when_mandatory_field_is_missing(self, data_for_create, code, response_body):
        response = requests.post(f"{Constants.base_url_page}{Constants.path_create_courier}", data=data_for_create)
        assert response.status_code == code and response.json()['message'] and response_body

    def test_cannot_create_user_with_duplicate_login(self):
        response = requests.post(f"{Constants.base_url_page}{Constants.path_create_courier}", data=Constants.data_duplicate_login_for_create_courier)
        assert response.status_code == 409 and response.json()['message'] == Constants.message_create_courier_duplicate_login