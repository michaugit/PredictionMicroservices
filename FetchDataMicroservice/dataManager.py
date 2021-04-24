import requests


# sprawdzenie czy obsługujemy taką walutę
def check_type(type):
    # to raczej by trzeba było pobrać z bazy danych
    types = ['zloto']
    return type in types


# pobranie określonego jsona (docelowo zapisanie go w bazie danych)
def fetch_data_from_nbp(type):
    if type == 'zloto':
        response = requests.get("http://api.nbp.pl/api/cenyzlota/last/30/?format=json")
        json_response = response.json()
        return json_response


# pobranie danych z bazy danych
def get_data_from_db(type):
    json_response = {"name": type, 'rates': fetch_data_from_nbp(type)}
    return json_response
