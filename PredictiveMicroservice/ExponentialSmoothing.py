from darts.models import ExponentialSmoothing
import matplotlib.pyplot as plt
import mpld3
import plotly

def predict(series, train, val):
    model = ExponentialSmoothing()
    model.fit(train)
    prediction = model.predict(len(val))

    series.plot(label='actual')
    prediction.plot(label='forecast', lw=3)
    plt.legend()

    fig = plt.figure()
    html_plot = mpld3.fig_to_html(fig)

    return html_plot