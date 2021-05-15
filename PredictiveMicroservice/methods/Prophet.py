from darts.models import Prophet
import predictorsProvider


def predict(df):
    series, train, val = predictorsProvider.split_data(df)
    model = Prophet()
    model.fit(train)
    prediction = model.predict(len(val))

    return predictorsProvider.prepare_plot(series, prediction, 'Method with Prophet model')

