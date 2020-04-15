import flask
from flask import Flask, request, jsonify
import json
import os
import requests
import pprint
app = Flask(__name__)
app.debug = True

import time
from selenium import webdriver

# def get_sunset_time(lng, date):
#     url = 'https://api.sunrise-sunset.org/json?lat=00.0000000&lng={}.0000000&date={}}'.format(lat, lng, date)
#     driver = webdriver.Chrome('chromedriver')
#     driver.get(url)
#     time.sleep(1)

def sunset_time_dispatch(req):
    date = req['queryResult']['outputContexts'][0]['parameters']['Date']
    date = date.split("T")
    date_num = date[0]
    # lng = date[1].split("-")[-1].split(":")[0]
    print(date)
    # get_sunset_time(date)
    return {'fulfillmentText': 'The Sunset will be at 9 PM.'}


@app.route('/', methods=['GET', 'POST'])
def do_stuff():
    req = request.json
    pprint.pprint(req)
    if 'sunset_time' in req['queryResult']['intent']['displayName']:
        return sunset_time_dispatch(req)


if __name__ == '__main__':
    # run back endpoint... default port 5001
    app.run(host='0.0.0.0', port=5001)


