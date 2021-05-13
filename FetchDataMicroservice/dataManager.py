import requests
import config
import dataMapper


def check_type(type_data):
    types = dataMapper.get_ids()
    return type_data in types


def get_data_from_db(type_data):
    json_data = dataMapper.get_json_data(type_data)
    json_response = {"name": type_data,
                     'rates': json_data}
    return json_response


def get_json(id):
    if id == 'GOLD':
        url = config.nbp_gold_ip
        response = requests.get(url)
        json_response = response.json()
    else:
        url = config.nbp_rates_ip.format(id)
        response = requests.get(url)
        json_response_tmp = response.json()
        json_response = []
        for record in json_response_tmp['rates']:
            json_response.append({'data': record['effectiveDate'], 'cena': record['mid']})

    return json_response


def fetch_data_from_nbp():
    ids = dataMapper.get_ids()
    for type_id in ids:
        json_response = get_json(type_id)
        dataMapper.update_db(json_response, type_id)


