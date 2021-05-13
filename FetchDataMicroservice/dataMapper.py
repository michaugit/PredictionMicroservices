from DatabaseConnector import DatabaseConnector


def get_ids():
    db = DatabaseConnector()
    data = db.execute_select("SELECT id FROM predictionDB.types ")
    type_ids = []
    for id_type in data:
        type_ids.append(id_type[0])

    return type_ids


def update_db(response, id):
    db = DatabaseConnector()
    for record in response:
        date = record['data']
        value = record['cena']

        data = db.execute_select(f"SELECT * FROM predictionDB.{id} WHERE date = '{date}' AND value = {value};")
        if not data:
            query = f"INSERT INTO predictionDB.{id} (date,value) VALUES ('{date}', {value });"
            db.execute_insert(query)


def get_json_data(id):
    db = DatabaseConnector()
    data = db.execute_select(f"SELECT * FROM predictionDB.{id} ORDER BY date DESC LIMIT 30;")
    json_data = []
    for record in data:
        json_data.append({"date": str(record[0]), "value": str(record[1])})

    return json_data
