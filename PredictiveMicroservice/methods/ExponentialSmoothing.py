from darts.models import ExponentialSmoothing
import predictorsProvider


def predict(df):
    series, train, val = predictorsProvider.split_data(df)
    model = ExponentialSmoothing()
    model.fit(train)
    prediction = model.predict(len(val))

    return predictorsProvider.prepare_plot(series, prediction, 'Method with ExponentialSmoothing model')

