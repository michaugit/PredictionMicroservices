from darts import TimeSeries
import dataProvider
from methods import ARIMA, AutoARIMA, ExponentialSmoothing, FFT, NaiveDrift, Prophet, ThetaMethod, NBEATS
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import pandas as pd


def tmp_predictor(to_predict, prediction_method):
    data = dataProvider.get_data(to_predict)
    df = prepare_data(data['rates'])
    if prediction_method == 'ExponentialSmoothing':
        json_response = {'html_code': ExponentialSmoothing.predict(df)}
    elif prediction_method == 'ARIMA':
        json_response = {'html_code': ARIMA.predict(df)}
    elif prediction_method == 'AutoARIMA':
        json_response = {'html_code': AutoARIMA.predict(df)}
    elif prediction_method == 'Prophet':
        json_response = {'html_code': Prophet.predict(df)}
    elif prediction_method == 'FFT':
        json_response = {'html_code': FFT.predict(df)}
    elif prediction_method == 'NaiveDrift':
        json_response = {'html_code': NaiveDrift.predict(df)}
    elif prediction_method == 'ThetaMethod':
        json_response = {'html_code': ThetaMethod.predict(df)}
    elif prediction_method == 'NBEATS':
        json_response = {'html_code': NBEATS.predict(df)}
    else:
        print("No such method found.")
    print(prediction_method)

    return json_response


def prepare_data(datae):
    df = pd.DataFrame.from_dict(datae)
    df.date = pd.to_datetime(df.date)
    df.value = pd.to_numeric(df.value)
    return df


def prepare_plot(series, prediction, title):
    fig = plt.figure()
    series.plot(label='actual', color='green', lw=2)
    prediction.plot(label='forecast', color='red', linestyle='--', lw=3)
    plt.xlabel('data')
    plt.ylabel('cena (zł)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    html_plot = mpld3.fig_to_html(fig)

    return html_plot


def split_data(df):
    df = df.set_index('date')
    df = df.reindex(pd.date_range(start=df.index[0], end=df.index[-1], freq='D'))
    df = df.fillna(method="pad", limit=5)
    df = df.reset_index()
    series = TimeSeries.from_dataframe(df, 'index', 'value', freq='B')
    print(series)
    train, val = series.split_before(pd.Timestamp(df.at[40, 'index']))
    return series, train, val

def tmp_matplotlib_html_generator():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig = plt.figure()

    plt.plot(t, s)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('EXAMPLE MATPLOTLIB')
    plt.grid(True)

    html_plot = mpld3.fig_to_html(fig)
    return html_plot
