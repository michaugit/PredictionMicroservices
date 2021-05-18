data_provider_ip = 'http://127.0.0.1:5001/getprediction/'

prediction_methods = {
    'ExponentialSmoothing': {'name': "ExponentialSmoothing",
                 'description': " Exponential Smoothing (proste wygładzanie wykładnicze). Ta metoda jest odpowiednia do prognozowania danych bez wyraźnego trendu lub wzorca sezonowego"},
    'ARIMA': {'name': "ARIMA",
                 'description': "ARIMA to skrót od autoregresywnej, zintegrowanej, ruchomej średniej. Model jest dopasowany do danych szeregów czasowych w celu lepszego zrozumienia danych lub przewidywania przyszłych punktów w szeregu. "},
    'AutoARIMA': {'name': "AutoARIMA",
                 'description': "Auto ARIMA (zintegrowany model autoregresyjny ze średnią ruchomą). Model auto-ARIMA ma na celu zidentyfikowanie najbardziej optymalnych parametrów ARIMA modelu, opierając się na pojedynczym dopasowanym modelu ARIMA."},
    'Prophet': {'name': "Prophet",
                 'description': "Prophet to procedura prognozowania danych szeregów czasowych w oparciu o model addytywny, w którym trendy nieliniowe są dopasowane do sezonowości rocznej, tygodniowej i dziennej oraz efektów świątecznych. Działa najlepiej w przypadku szeregów czasowych, które mają silne efekty sezonowe i kilka sezonów danych historycznych. Prophet jest odporny na brak danych i zmiany trendu i zazwyczaj dobrze radzi sobie z wartościami odstającymi."},
    'FFT': {'name': "FFT",
                 'description': "FFT - model ten wykonuje prognozowanie na instancji TimeSeries przy użyciu FFT, późniejsze filtrowanie częstotliwości i odwrotną FFT, połączone z opcją określenia danych i przycinania sekwencji uczącej do pełnych okresów sezonowych . Należy pamiętać, że sekwencja ucząca nie może zawierać żadnych wartości NaN, aby model generował użyteczne dane wyjściowe."},
    # 'NaiveDrift': {'name': "NaiveDrift",
    #              'description': "opis metody 6"},
    'ThetaMethod': {'name': "ThetaMethod",
                 'description': "Theta to dość nowa jednoczynnikowa metoda prognozowania. Metoda opiera się na koncepcji modyfikacji lokalnej krzywizny szeregów czasowych za pomocą współczynnika Theta (grecka litera θ), który jest stosowany bezpośrednio do drugich różnic w danych"},
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
            },
    'aud': {
                'link': "aud",
                "title": "Dolar Australijski",
                "description": "Jakiś opis opisujący aud",
                "default_prediction_method": prediction_methods['ExponentialSmoothing'],
                "prediction_methods": prediction_methods
            },
    'gbp': {
                'link': "gbp",
                "title": "Funt Szterling",
                "description": "Jakiś opis opisujący gbp",
                "default_prediction_method": prediction_methods['ExponentialSmoothing'],
                "prediction_methods": prediction_methods
            },
    'chf': {
                'link': "chf",
                "title": "Frank Szwajcarski",
                "description": "Jakiś opis opisujący chf",
                "default_prediction_method": prediction_methods['ExponentialSmoothing'],
                "prediction_methods": prediction_methods
            },
    'jpy': {
                'link': "jpy",
                "title": "Jen (Japonia)",
                "description": "Jakiś opis opisujący jen",
                "default_prediction_method": prediction_methods['ExponentialSmoothing'],
                "prediction_methods": prediction_methods
            },
    'czk': {
                'link': "czk",
                "title": "Korona Czeska",
                "description": "Jakiś opis opisujący czk",
                "default_prediction_method": prediction_methods['ExponentialSmoothing'],
                "prediction_methods": prediction_methods
            }
}


