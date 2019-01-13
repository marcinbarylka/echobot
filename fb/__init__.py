import json

import requests
from settings import FB_PAGE_ACCESS_TOKEN


def post_facebook_message(fbid, received_message):
    post_message_url = f'https://graph.facebook.com/v3.1/me/messages?' \
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
