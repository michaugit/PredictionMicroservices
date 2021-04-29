import dataProvider
import matplotlib.pyplot as plt
import numpy as np
import mpld3


def tmp_predictor(to_predict, prediction_method):
    data = dataProvider.get_data(to_predict)
    # print(data)
    json_response = {'html_code': tmp_matplotlib_html_generator()}
    return json_response


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
