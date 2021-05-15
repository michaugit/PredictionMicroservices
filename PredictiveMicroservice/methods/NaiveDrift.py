from darts.models import NaiveDrift
import predictorsProvider


def predict(df):
    series, train, val = predictorsProvider.split_data(df)
    model = NaiveDrift()
    model.fit(train)
    prediction = model.predict(len(val))

    return predictorsProvider.prepare_plot(series, prediction, 'Method with NaiveDrift model')

