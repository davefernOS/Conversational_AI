from flask import Flask, request, jsonify
import json
import requests
import pprint
app = Flask(__name__)
app.debug = True

last_city = 'NONE'

@app.route('/', methods=['POST'])
def start():
    # maintain last city mentioned in last_city
    global last_city

    # get payload
    content = request.json

    # for print debugging
    pprint.pprint(content)

    # sanity check.  Don't do anything if we're not in the 'weather' state
    if content['state'] != 'weather':
        return jsonify(content)

    # retrieve the slot
    the_city = content['slots']['_CITY_']['values'][0]['tokens'] 

    # resolve the slot (if it's not resolved, the platform may complain in the response)
    content['slots']['_CITY_']['values'][0]['resolved'] = 1

    #map it (in this case, the slot is mapped to the token)
    content['slots']['_CITY_']['values'][0]['value'] = the_city

    print '####'

    if the_city == last_city:
        # if they mentioned this city before, go to test2
        new_state = 'test2'
    else:
        # otherwise, to to test
        new_state = 'test'

    print 'new_state : {}'.format(new_state)
    print '####'

    # update our history
    last_city = the_city

    # change state in payload... platform will use this to decide where to go
    content['state'] = new_state
    pprint.pprint(content)
    print '#############################\n\n\n'

    #platform accepts the modified JSON payload.
    return jsonify(content)

if __name__ == '__main__':
    # run BLS endpoint... default port 5000
    app.run(host='0.0.0.0', port=5000)
