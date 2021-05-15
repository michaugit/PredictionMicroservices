from darts.models import FFT
import predictorsProvider


def predict(df):
    series, train, val = predictorsProvider.split_data(df)
    model = FFT()
    model.fit(train)
    prediction = model.predict(len(val))

    return predictorsProvider.prepare_plot(series, prediction, 'Method with FFT model')

