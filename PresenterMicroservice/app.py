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

    html_matplotlib, mse, ope, coe = dataProvider.get_prediction(to_predict, prediction_method)

    return render_template('prediction_details.html',
                           config=config.prediction_types[to_predict],
                           prediction_method=prediction_method,
                           prediction_html=html_matplotlib,
                           mse=mse,
                           ope=ope,
                           coe=coe)


if __name__ == '__main__':
    app.run()
