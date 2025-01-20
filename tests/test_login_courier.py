import pytest
import requests

from data.constants import Constants
from helpers.data_for_create_courier import GenerateData


class TestLoginCourier:
    def test_successful_authorization(self):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_login_courier}', data=Constants.data_for_authorization)
        assert response.status_code == 200 and response.json()['id'] == Constants.id_successful_authorization

    @pytest.mark.parametrize('payload, code, key, response_body', [[Constants.data_for_authorization, 200, 'id', Constants.id_successful_authorization], [Constants.data_for_authorization_without_login, 400, 'message', Constants.message_missing_parameters], [Constants.data_for_authorization_without_password, 400, 'message', Constants.message_missing_parameters]])
    def test_authorization_requires_all_mandatory_fields(self, payload, code, key, response_body):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_login_courier}', data=payload)
        assert response.status_code == code and response.json()[key] == response_body

    @pytest.mark.parametrize('payload', [{'login': 'olegShadrikov', 'password': f'{GenerateData.generate_random_string(10)}'}, {'login': f'{GenerateData.generate_random_string(10)}', 'password': '1234567890'}])
    def test_login_fails_with_incorrect_credentials(self, payload):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_login_courier}', data=payload)
        assert response.status_code == 404 and response.json()['message'] == Constants.message_account_not_found

    @pytest.mark.parametrize('payload, code, response_body', [[Constants.data_for_authorization_without_login, 400, Constants.message_missing_parameters], [Constants.data_for_authorization_without_password, 400, Constants.message_missing_parameters]])
    def test_authorization_fails_with_missing_required_fields(self, payload, code, response_body):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_login_courier}', data=payload)
        assert response.status_code == code and response.json()['message'] == response_body

    def test_error_returned_for_nonexistent_user(self):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_login_courier}', data=GenerateData.create_data())
        assert response.status_code == 404 and response.json()['message'] == Constants.message_account_not_found

    def test_successful_authorization_returns_user_id(self):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_login_courier}', data=Constants.data_for_authorization)
        assert response.json()['id'] == Constants.id_successful_authorization and response.status_code == 200