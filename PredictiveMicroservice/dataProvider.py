import config
import requests


def get_data(to_predict):
    response = requests.get(config.data_provider_ip + to_predict)
    json_response = response.json()
    return json_response
