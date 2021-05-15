from darts.models import ARIMA
import predictorsProvider


def predict(df):
    series, train, val = predictorsProvider.split_data(df)
    model = ARIMA()
    model.fit(train)
    prediction = model.predict(len(val))

    return predictorsProvider.prepare_plot(series, prediction, 'Method with ARIMA model')

