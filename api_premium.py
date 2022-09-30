import requests
from settings_premium import key
from settings_premium import msisdn
from settings_premium import userID
import json

class Premium:
    def __init__(self):
        self.base_url = "https://dev-premium.mts.ru/"

    def get_available_msisdn(self, key=key):

        headers = {'x-token': key}

        res = requests.get(self.base_url + 'api/sub/v1/subscriptions/available/' + msisdn, headers=headers, verify=False)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_active_msisdn(self, key=key):

        headers = {'x-token': key}

        res = requests.get(self.base_url + 'api/sub/v1/subscriptions/active/' + msisdn, headers=headers, verify=False)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_profiles_msisdn(self, key=key):

        headers = {'x-token': key}

        res = requests.get(self.base_url + 'api/sub/v1/profiles/' + msisdn, headers=headers, verify=False)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_available(self, key=key, userID=userID):

        headers = {'x-token': key}
        params = {
            "userID": userID
        }

        res = requests.get(self.base_url + 'api/sub/v1/subscriptions/available/', params=params, headers=headers, verify=False)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_active(self, key=key, userID=userID):

        headers = {'x-token': key}
        params = {
            "userID": userID
        }

        res = requests.get(self.base_url + 'api/sub/v1/subscriptions/active/', params=params, headers=headers, verify=False)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_profiles(self, key=key):

        headers = {'x-token': key}

        res = requests.get(self.base_url + 'api/sub/v1/profiles/' + msisdn + '/status', headers=headers, verify=False)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result