from darts.models import ExponentialSmoothing
import matplotlib.pyplot as plt
import mpld3
import plotly
from darts import TimeSeries
import pandas as pd
from darts.models import FFT

def predict(df):
    series, train, val = split_data(df)
    model = FFT()
    model.fit(train)
    prediction = model.predict(len(val))
    fig = plt.figure()
    series.plot(label='actual')
    prediction.plot(label='forecast', lw=3)
    plt.xlabel('data')
    plt.ylabel('cena (zł)')
    plt.title('FFT method')
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
    train, val = series.split_before(pd.Timestamp(df.at[33, 'index']))
    return series, train, val