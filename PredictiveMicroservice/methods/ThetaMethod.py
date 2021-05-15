from darts.models import FourTheta

import predictorsProvider


def predict(df):
    series, train, val = predictorsProvider.split_data(df)
    model = FourTheta(3)
    model.fit(train)
    prediction = model.predict(len(val))

    return predictorsProvider.prepare_plot(series, prediction, 'Method with Theta model')
