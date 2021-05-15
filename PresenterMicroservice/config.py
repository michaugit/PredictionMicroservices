data_provider_ip = 'http://127.0.0.1:5001/getprediction/'

prediction_methods = {
    'ExponentialSmoothing': {'name': "ExponentialSmoothing",
                 'description': "opis metody 1"},
    'ARIMA': {'name': "ARIMA",
                 'description': "opis metody 2"},
    'AutoARIMA': {'name': "AutoARIMA",
                 'description': "opis metody 3"},
    'Prophet': {'name': "Prophet",
                 'description': "opis metody 4"},
    'FFT': {'name': "FFT",
                 'description': "opis metody 5"},
    'NaiveDrift': {'name': "NaiveDrift",
                 'description': "opis metody 6"},
    'ThetaMethod': {'name': "ThetaMethod",
                 'description': "opis metody 7"},
    # 'NBEATS': {'name': "NBEATS",
    #                 'description': "opis metody 8"},
}

prediction_types = {
    'gold': {
                'link': "gold",
                "title": "Złoto",
                "description": "Jakiś opis opisujący złoto",
                "default_prediction_method": prediction_methods['ExponentialSmoothing'],
                "prediction_methods": prediction_methods
            },
    'usd': {
                'link': "usd",
                "title": "Dolar Amerykański",
                "description": "Jakiś opis opisujący usd",
                "default_prediction_method": prediction_methods['ExponentialSmoothing'],
                "prediction_methods": prediction_methods
            }
}


