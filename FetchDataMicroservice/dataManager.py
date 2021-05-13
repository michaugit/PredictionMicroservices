import requests


# sprawdzenie czy obsługujemy taką walutę
from DatabaseConnector import DatabaseConnector


def check_type(type_data):
    # to raczej by trzeba było pobrać z bazy danych
    type_datas = ['gold', 'usd']
    return type_data in type_datas


# pobranie określonego jsona (docelowo zapisanie go w bazie danych)
def fetch_data_from_nbp(type_data):
    if type_data == 'gold':
        response = requests.get("http://api.nbp.pl/api/cenyzlota/last/30/?format=json")
        json_response = response.json()
        return json_response
    else:
        return {'empty': 'empty'}


# pobranie danych z bazy danych
def get_data_from_db(type_data):
    json_response = {"name": type_data,
                     'rates': fetch_data_from_nbp(type_data)}
    return json_response


# wykonanie odpowiednich zapytań do nbp i zapisanie ich w bazie danych
# działa to asynchronicznie w tle np. raz na dzień aby updatować baze danych
# docelowo będą tutaj wywoływane funkcje do pobrania jsonow z nbp coś w stylu jak fetch_data_from_nbp()
def background_periodic_task():
    db = DatabaseConnector()
    data = db.execute("SELECT * FROM predictionDB.types ")
    # print(data)
    for record in data:
        print(record)
    print("Start background periodic task fetching data from nbp and saving it to our DB")
