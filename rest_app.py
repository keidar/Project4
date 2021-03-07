from datetime import datetime
from flask import Flask, request
from db_connector import *
import random
import signal
import os

app = Flask(__name__)


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        try:
            name = get_user_id(user_id)
            return {'status': 'ok', 'user name': name}, 200
        except:
            return {'status': 'error', 'reason': "no such id"}, 500  # status code

    elif request.method == 'POST':
        try:
            time = datetime.now()
            time = time.strftime("%Y-%m-%d %H:%M:%S %p")
            # getting the json data payload from request
            request_data = request.json

            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            insert_user(user_id, user_name, time)
            return {'status': 'ok', 'user added': user_name}, 201  # status code
        except(pymysql.err.IntegrityError):
            res = get_all_users_ids()
            num = random.randint(1000,9999)
            while num in res:
                num = random.randint(1000, 9999)
                insert_user(num, user_name, time)
            return {'status': 'Info', 'reason': f"id already exist inserted  id {num} instead "}, 201  # status code

    elif request.method == 'PUT':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            get_user_id(user_id)
            update_user(user_name, user_id)
            return {'status': 'ok', 'user_updated': user_name}, 200  # status code
        except:
            return {'status': 'error', 'reason': "no such id"}, 500
    elif request.method == 'DELETE':
        try:
            get_user_id(user_id)
            delete_user(user_id)
            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
        except:
            return {'status': 'error', 'reason': "no such id"}, 500


def stop_server():
    try:
        os.kill(os.getpid(), signal.SIGINT)
        return 'Server stopped', 200

    except:
        return {'status': 'error', 'reason': "didn't manage to close rest app'"}, 500

@app.route('/hello')
def hello():
    return {'status': 'ok', 'user added': 'keidar'}, 201  # status code


app.run(host='0.0.0.0', debug=True)
