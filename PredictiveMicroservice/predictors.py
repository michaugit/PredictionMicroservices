import dataProvider, ThetaMethod, FFT
import ExponentialSmoothing
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import pandas as pd



def tmp_predictor(to_predict, prediction_method):
    data = dataProvider.get_data(to_predict)
    df = prepare_data(data['rates'])
    if prediction_method == 'metoda_1':
        json_response = {'html_code': ExponentialSmoothing.predict(df)}
    elif prediction_method == 'metoda_2':
        json_response = {'html_code': ThetaMethod.predict(df)}
    elif prediction_method == 'metoda_3':
        json_response = {'html_code': FFT.predict(df)}
    else: print("kupa")
    print(prediction_method)

    return json_response


def prepare_data(datae):
    df = pd.DataFrame.from_dict(datae)
    # print(df)
    df.date = pd.to_datetime(df.date)
    df.value = pd.to_numeric(df.value)
    return df


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