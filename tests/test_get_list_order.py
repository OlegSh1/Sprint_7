import requests
from data.constants import Constants

class TestGetListOrder:
    def test_get_list_order(self):
        response = requests.get(f'{Constants.base_url_page}{Constants.path_get_list_order}{Constants.id_successful_authorization}')
        assert response.json()['orders'] == Constants.orders and response.status_code == 200