from darts.models import NBEATSModel, StandardRegressionModel


import predictorsProvider
from darts import TimeSeries


def predict(df):
    series, train, val, series_row = predictorsProvider.split_data(df)
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
    pred = TimeSeries.append(series_row, prediction)
    return series, pred

