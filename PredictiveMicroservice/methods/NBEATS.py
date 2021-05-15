from darts.models import NBEATSModel, StandardRegressionModel
import matplotlib.pyplot as plt
import mpld3
import plotly
from darts import TimeSeries
import pandas as pd
from darts.models import FFT
from sklearn.linear_model import LinearRegression

import predictorsProvider


def predict(df):
    series, train, val = predictorsProvider.split_data(df)
    model = NBEATSModel(
        input_chunk_length=30,
        output_chunk_length=7,
        generic_architecture=True,
        num_stacks=10,
        num_blocks=1,
        num_layers=4,
        layer_widths=512,
        n_epochs=100,
        nr_epochs_val_period=1,
        batch_size=800,
        model_name='nbeats_run'
    )

    model.fit(train, val_series=val, verbose=True)
    prediction = model.predict(len(val))

    return predictorsProvider.prepare_plot(series, prediction, 'Method with Prophet model')

