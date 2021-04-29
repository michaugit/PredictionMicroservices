import requests
import config


def get_prediction(to_predict, prediction_method):
    response = requests.get(config.data_provider_ip + to_predict + "/" + prediction_method)
    json_response = response.json()
    html_matplotlib = json_response['html_code']
    return html_matplotlib
