import requests
import json
import os


def getServerList():
    auth_url = "https://www.digitalcombatsimulator.com/en/auth/"
    payload = {
        'AUTH_FORM': 'Y',
        'TYPE': 'AUTH',
        'backurl': '/en/personal/server/?ajax=y',
        'USER_LOGIN': os.environ["DCS-USERNAME"],
        'USER_PASSWORD': os.environ["DCS-PASSWORD"],
        'USER_REMEMBER': 'Y'
    }

    r = requests.post(auth_url, data=payload)

    server_info = json.loads(r.text)
    return server_info
