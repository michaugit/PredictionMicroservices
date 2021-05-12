from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import json, dataManager, datetime

app = Flask(__name__)


@app.route('/getdatafromdb/<type_data>', methods=['GET'])
def get_data_from_db(type_data):
    response = app.response_class(status=404)

    if dataManager.check_type(type_data):
        data = dataManager.get_data_from_db(type_data)

        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    return response


def background_task_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(dataManager.background_periodic_task, 'interval', seconds=10, next_run_time=datetime.datetime.now())
    scheduler.start()


if __name__ == '__main__':
    app.run()
background_task_scheduler()
