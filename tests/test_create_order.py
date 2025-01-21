import pytest
import requests

from data.constants import Constants
from helpers.data_for_create_courier import GenerateData


class TestCreateOrder:
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY']])
    def test_color_can_be_black_or_grey(self, color):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_create_order}', data=GenerateData.crate_data_for_create_order(color))
        assert response.status_code == 201

    def test_accepts_black_and_grey_as_valid_colors(self):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_create_order}', data=GenerateData.crate_data_for_create_order(['BLACK', 'GREY']))
        assert response.status_code == 201

    def test_order_creation_without_color_is_successful(self):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_create_order}', data=GenerateData.crate_data_for_create_order([]))
        assert response.status_code == 201

    def test_response_contains_track(self):
        response = requests.post(f'{Constants.base_url_page}{Constants.path_create_order}', data=GenerateData.crate_data_for_create_order([]))
        assert 'track' in response.json()
        assert response.status_code == 201