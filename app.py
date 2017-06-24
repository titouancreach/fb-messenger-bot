from fbmessage import FBMessagingEvent
from flask import Flask, request

import json
import os
import requests
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    """
    Callback called when someone do a GET request on /.
    """
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if not request.args.get('hub.verify_token') == os.environ['VERIFY_TOKEN']:
            return 'Verification token mismatch', 403
        return request.args['hub.challenge'], 200
    return 'Only facebook request are working', 400


@app.route('/', methods=['POST'])
def webhook():
    """
    Callback called when someone do a POST request on /.
    """
    data = request.get_json()

    print(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            fbevents = [FBMessagingEvent(rawevent) for rawevent in entry['messaging']]

            for ev in fbevents:
                ev.respond('Bonjour numéro: {} :)'.format(str(ev.sender_id)))

    return 'ok', 200


if __name__ == '__main__':
    app.run(debug=True)
