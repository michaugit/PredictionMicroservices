from darts import TimeSeries
import dataProvider, checkResults
from methods import ARIMA, AutoARIMA, ExponentialSmoothing, FFT, NaiveDrift, Prophet, ThetaMethod, NBEATS
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import pandas as pd


def tmp_predictor(to_predict, prediction_method):
    data = dataProvider.get_data(to_predict)
    df = prepare_data(data['rates'])

    try:
        series, pred = eval(prediction_method).predict(df)
        mse, ope, coe = checkResults.checkMetrics(series, pred, 10)
        json_response = {'html_code': prepare_plot(series, pred, 'Method with ' + prediction_method + ' model'),
                         'mse': mse,
                         'ope': ope,
                         'coe': coe}
    except:
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
    prediction.plot(label='forecast', color='red', lw=3)
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
    number_days_to_predict = 10
    index_to_split = len(series) - number_days_to_predict
    train, val = series.split_before(pd.Timestamp(df.at[index_to_split, 'index']))
    train_last_date = take_train_last_date(df, index_to_split)
    return series, train, val, train_last_date

def take_train_last_date(df, index_to_split):
    new_row = pd.DataFrame([df['value'][index_to_split - 1]], columns=['0'], index=[df['index'][index_to_split - 1]])
    series_row = TimeSeries.from_dataframe(new_row, freq='D')
    return series_row