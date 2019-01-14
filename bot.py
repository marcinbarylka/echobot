import json
from pprint import pprint

from flask import Flask, request

from fb import post_facebook_message
from settings.fb_local_settings import FB_VERIFY_TOKEN

app = Flask(__name__)


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
                if 'text' in message['message']:
                    post_facebook_message(message['sender']['id'],
                                          message['message']['text'])
                else:
                    post_facebook_message(message['sender']['id'],
                                          "obrazki")
    return ""


if __name__ == "__main__":
    app.run(debug=True)
