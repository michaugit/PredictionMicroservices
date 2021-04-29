prediction_methods = {
    'metoda_1': {'name': "metoda_1",
                 'description': "opis metody 1"},
    'metoda_2': {'name': "metoda_2",
                 'description': "opis metody 2"},
    'metoda_3': {'name': "metoda_3",
                 'description': "opis metody 3"}
}

prediction_types = {
    'gold': {
                'link': "gold",
                "title": "Złoto",
                "description": "Jakiś opis opisujący złoto",
                "default_prediction_method": prediction_methods['metoda_1'],
                "prediction_methods": prediction_methods
            },
    'usd': {
                'link': "usd",
                "title": "Dolar Amerykański",
                "description": "Jakiś opis opisujący usd",
                "default_prediction_method": prediction_methods['metoda_1'],
                "prediction_methods": prediction_methods
            }
}


