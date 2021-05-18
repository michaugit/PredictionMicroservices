from darts.models import ARIMA
import predictorsProvider
from darts import TimeSeries

def predict(df):
    series, train, val, series_row = predictorsProvider.split_data(df)
    model = ARIMA(p=1, d=3, q=5)
    model.fit(train)
    prediction = model.predict(len(val))
    pred = TimeSeries.append(series_row, prediction)
    return series, pred

