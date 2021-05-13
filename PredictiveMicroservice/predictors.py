import dataProvider
import ExponentialSmoothing
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import pandas as pd
from darts import TimeSeries


def tmp_predictor(to_predict, prediction_method):
    data = dataProvider.get_data(to_predict)
    print(data)
    series, train, val = prepare_data(data)
    if prediction_method == 'metoda_1':
        json_response = {'html_code': ExponentialSmoothing.predict(series, train, val)}
        print(json_response)
    elif prediction_method == 'metoda_2':
        print("XD")
    else: print("kupa")
    print(prediction_method)

    return json_response


def prepare_data(datae):

    df = pd.DataFrame.from_dict(datae['rates'])
    print(df)
    df.data = pd.to_datetime(df.data)
    df = df.set_index('data')
    df = df.reindex(pd.date_range(start=df.index[0], end=df.index[-1], freq='D'))
    df = df.reindex(pd.date_range(start=df.index[0], end=df.index[-1], freq='D'))
    df = df.fillna(method="pad", limit=5)
    df = df.reset_index()
    series = TimeSeries.from_dataframe(df, 'index', 'cena', 'D')
    train, val = series.split_before(pd.Timestamp(df.at[33, 'index']))
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
