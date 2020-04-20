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

#default values
lat_def = -12.6168449
lng_def = -38.0578038

def get_tide_times(date):
    database = settings.get_db()
    db_cursor = database.cursor()
    db_cursor.execute('SELECT * FROM posts WHERE the_date={}'.format(date))
    tide_times = db_cursor.fetchone()


def time_offset(lat, lng):
    time_offset_url = 'https://maps.googleapis.com/maps/api/timezone/json?location={},{}&timestamp=0&key=AIzaSyDFU96TE1zMjZi5Cnu3QRPsOP9l2bcbNFY'.format(lat, lng)
    req = requests.get(url=time_offset_url).json()
    pprint.pprint(req)
    # print("time_offset: {} --------------------------".format())

def get_sunset_sunrise_api_data(date, lat, lng):
    URL = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&date={}'.format(lat, lng, date)
    req = requests.get(url = URL).json()
    # pprint.pprint(req) 
    # time_offset(lat, lng)
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
def backend_dispatch():
    req = request.json
    pprint.pprint(req) # Uncomment to see the POST request send by Dialogflow
    if 'sunset_time' in req['queryResult']['intent']['displayName']:
        return sunset_time_dispatch(req)
    elif 'tide' in req['queryResult']['intent']['displayName']:
        return get_tide_times(date)


if __name__ == '__main__':
    # run back endpoint... default port 5001
    app.run(host='0.0.0.0', port=5001)

