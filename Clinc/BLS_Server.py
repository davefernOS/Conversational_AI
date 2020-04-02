import flask
from flask import Flask, request, jsonify
import json
import requests
app = Flask(__name__)
app.debug = True

context = {}



@app.route('/', methods=['GET', 'POST'])
def show_index():
    """Show the index page."""
    context = {}
    return flask.render_template("index.html", **context)

@app.route('/speech/', methods=['GET', 'POST'])
def show_speech_pre():
    """Show the index page."""
    if flask.request.method == 'POST':
        context['message'] = flask.session['message']

    context = {
            'status': 'Testing Messages',
            'status_code': 200
    }
    return flask.jsonify(**context)

if __name__ == '__main__':
    # run BLS endpoint... default port 5000
    app.run(host='0.0.0.0', port=5000)
