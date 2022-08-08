import requests
from settings import key
from settings import msisdn
import json

class Premium:
    def __init__(self):
        self.base_url = "https://dev-premium.mts.ru/"

    def get_available(self, key=key):

        headers = {'x-token': key}

        res = requests.get(self.base_url + 'api/sub/v1/subscriptions/available/' + msisdn, headers=headers, verify=False)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_active(self, key=key):

        headers = {'x-token': key}

        res = requests.get(self.base_url + 'api/sub/v1/subscriptions/available/' + '79859186246', headers=headers, verify=False)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result
