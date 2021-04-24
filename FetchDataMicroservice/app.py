from flask import Flask
import json, dataManager

app = Flask(__name__)

@app.route('/getdatafromdb/<type_data>', methods=['GET'])
def getDataFromDB(type_data):
    response = app.response_class(status=404)

    if dataManager.check_type(type_data):
        data = dataManager.get_data_from_db(type_data)

        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    return response



if __name__ == '__main__':
    app.run()





