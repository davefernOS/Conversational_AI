import flask
from flask import Flask, request, jsonify
import requests
import json
import os
import requests
import pprint
import datetime
app = Flask(__name__)
app.debug = True

import settings

# Response sent to dialog flow to fulfill the specific query/intent 
context = {"response": ""}

#
PARAMS_Q = {
                "lang": "en",
                "query": "",
                "contexts": [{"name": "location", "parameters": {"latitude": 0, "longitude": 0}}],
                "sessionId": "12345",
                "timezone": "America/New_York"
            }

HEAD_Q  =  { 'Authorization' :  'Bearer 078e4cb8210243e8b7327c987d60d3e2' }

URL_Q = 'https://api.dialogflow.com/v1/query?v=20150910'

@app.route('/', methods=['GET', 'POST'])
def show_index():
    """Show the index page."""
    return flask.render_template("index.html", **context)

@app.route('/demo/', methods=['GET', 'POST'])
def show_demo():
    """Show the index page."""
    return flask.render_template("demo.html", **context)

@app.route('/speech/', methods=['GET', 'POST'])
def show_speech():
    """Show the index page."""
    if flask.request.method == 'POST':
        query = flask.request.form["query"]
        lat = flask.request.form["lat"]
        lng = flask.request.form["lng"]
        settings.edit_loc(lat, lng)
        print(query)
        print(settings.get_loc(), "  Time:   ", datetime.datetime.now())
        PARAMS_Q['query'] = query
        req = requests.get(url = URL_Q, params = PARAMS_Q, headers = HEAD_Q).json()
        pprint.pprint(req)
        context["response"] = req["result"]["fulfillment"]["speech"]
    return flask.render_template("web_speech.html", **context)



if __name__ == '__main__':
    # run front endpoint... default port 5000
    app.run(host='0.0.0.0', port=5000)


