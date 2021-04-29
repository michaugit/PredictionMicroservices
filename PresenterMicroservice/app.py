from flask import Flask, render_template

import config

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html',
                           prediction_types=config.prediction_types)


@app.route('/<to_predict>/<prediction_method>')
def details(to_predict, prediction_method):

    prediction_plot_html = "<p>WYKRES dla " + prediction_method + "</p>" #html otrzymany z jsona od flaska 2

    return render_template('prediction_details.html',
                           config=config.prediction_types[to_predict],
                           prediction_method=prediction_method,
                           prediction_html=prediction_plot_html)


if __name__ == '__main__':
    app.run()
