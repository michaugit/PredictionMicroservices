import requests


# sprawdzenie czy obsługujemy taką walutę
def check_type(type_data):
    # to raczej by trzeba było pobrać z bazy danych
    type_datas = ['zloto']
    return type_data in type_datas


# pobranie określonego jsona (docelowo zapisanie go w bazie danych)
def fetch_data_from_nbp(type_data):
    if type_data == 'zloto':
        response = requests.get("http://api.nbp.pl/api/cenyzlota/last/30/?format=json")
        json_response = response.json()
        return json_response


# pobranie danych z bazy danych
def get_data_from_db(type_data):
    json_response = {"name": type_data,
                     'rates': fetch_data_from_nbp(type_data)}
    return json_response
