from darts.models import AutoARIMA
import predictorsProvider


def predict(df):
    series, train, val = predictorsProvider.split_data(df)
    model = AutoARIMA()
    model.fit(train)
    prediction = model.predict(len(val))

    return predictorsProvider.prepare_plot(series, prediction, 'Method with AutoARIMA model')
