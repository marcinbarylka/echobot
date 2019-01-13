# verify token:
# c1215981fdbf49949a578b41d0235204
import json
from pprint import pprint

import requests
from flask import Flask, request

from local_settings import FB_PAGE_ACCESS_TOKEN, FB_VERIFY_TOKEN

app = Flask(__name__)


def post_facebook_message(fbid, received_message):
    post_message_url = f'https://graph.facebook.com/v2.6/me/messages?' \
        f'access_token={FB_PAGE_ACCESS_TOKEN}'
    response_msg = json.dumps({
        "recipient": {"id": fbid},
        "message": {
            "text": f"Chyba twoja stara {received_message}"
        }
    })
    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=response_msg)
    return status


@app.route("/bot/d9417da2cbc8499f82db7649685133d8", methods=["GET"])
def web_hook_register():
    if request.args.get('hub.verify_token') == FB_VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    else:
        return 'Error, invalid token'


@app.route("/bot/d9417da2cbc8499f82db7649685133d8", methods=["POST"])
def web_hook():
    incoming_message = json.loads(request.data)
    for entry in incoming_message['entry']:
        for message in entry['messaging']:
            if 'message' in message:
                pprint(message)
                post_facebook_message(message['sender']['id'],
                                      message['message']['text'])
    return ""


if __name__ == "__main__":
    app.run(debug=True)
