import flask
from flask import Flask, request, jsonify
import json
import os
import requests
import pprint
app = Flask(__name__)
app.debug = True

import datetime
import settings

lat_def = -12.6168449
lng_def = -38.0578038

def get_sunset_sunrise_api_data(date, lat, lng):
    URL = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&date={}'.format(lat, lng, date)
    req = requests.get(url = URL).json()
    pprint.pprint(req)
    return req

def sunset_time_dispatch(req):
    date = req['queryResult']['outputContexts'][0]['parameters']['Date']
    date = date.split("T")[0]
    location = settings.get_loc()
    lat = location[0]
    lng = location[1]
    print(settings.get_loc(), "++++++++++++++++++++")
    results = get_sunset_sunrise_api_data(date, lat, lng)['results']
    return {'fulfillmentText': 'The Sunset will be at {}.'.format(results['sunset'])}
    


@app.route('/', methods=['GET', 'POST'])
def do_stuff():
    req = request.json
    # pprint.pprint(req)
    if 'sunset_time' in req['queryResult']['intent']['displayName']:
        return sunset_time_dispatch(req)


if __name__ == '__main__':
    # run back endpoint... default port 5001
    app.run(host='0.0.0.0', port=5001)

