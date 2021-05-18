from darts.models import NaiveDrift
import predictorsProvider
from darts import TimeSeries


def predict(df):
    series, train, val,series_row = predictorsProvider.split_data(df)
    model = NaiveDrift()
    model.fit(train)
    prediction = model.predict(len(val))
    pred = TimeSeries.append(series_row, prediction)
    return series, pred

