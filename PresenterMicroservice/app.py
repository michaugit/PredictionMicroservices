from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    prediction_types = ['zloto']
    return render_template('main.html', prediction_types=prediction_types)


if __name__ == '__main__':
    app.run()
