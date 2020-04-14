import flask
from flask import Flask, request, jsonify
import json
import os
import requests
app = Flask(__name__)
app.debug = True

context = {}

link_base = "https://api.dialogflow.com/v1/"

dev_key = "76c46ddde3ea4f269f16a35d3443e758"

client_key = "ca63929f74224859a3ab7bf70e82062f"

static_folder = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'static'
)


@app.route('/', methods=['GET', 'POST'])
def show_index():
    """Show the index page."""
    return flask.render_template("index.html", **context)

@app.route('/demo/', methods=['GET'])
def show_demo():
    """Show the index page."""
    return flask.render_template("demo.html", **context)

@app.route('/speech/', methods=['GET'])
def show_speech():
    """Show the index page."""
    return flask.render_template("web_speech.html", **context)

@app.route('/uploads/<img_url>')
def get_img_url(img_url):
    """Get the URL for img_url."""
    
    return flask.send_from_directory(static_folder, img_url)



if __name__ == '__main__':
    # run BLS endpoint... default port 5000
    app.run(host='0.0.0.0', port=5000)


