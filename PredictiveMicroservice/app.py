import json

from flask import Flask
import requests
import predictorsProvider

app = Flask(__name__)


@app.route('/getprediction/<to_predict>/<prediction_method>', methods=['GET'])
def get_prediction(to_predict, prediction_method):
    data = predictorsProvider.tmp_predictor(to_predict, prediction_method)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
