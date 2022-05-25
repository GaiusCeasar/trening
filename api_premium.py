import requests

import json

class Premium:
    def __init__(self):
        self.base_url = "https://dev-premium.mts.ru/"

    def get_available(self, token):

        headers = {'x-token': token['key']}

        res = requests.get(self.base_url + 'api/sub/v1/subscriptions/available', headers=headers)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result