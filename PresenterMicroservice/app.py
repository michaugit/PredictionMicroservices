from flask import Flask, render_template

import config
import dataProvider

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html',
                           prediction_types=config.prediction_types)


@app.route('/<to_predict>/<prediction_method>')
def details(to_predict, prediction_method):

    prediction_plot_html = dataProvider.get_prediction(to_predict, prediction_method)

    return render_template('prediction_details.html',
                           config=config.prediction_types[to_predict],
                           prediction_method=prediction_method,
                           prediction_html=prediction_plot_html)


if __name__ == '__main__':
    app.run()
