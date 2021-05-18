from darts.models import FourTheta
from darts import TimeSeries

import predictorsProvider


def predict(df):
    series, train, val, series_row = predictorsProvider.split_data(df)
    model = FourTheta(3)
    model.fit(train)
    prediction = model.predict(len(val))
    pred = TimeSeries.append(series_row, prediction)
    return series, pred
