import requests
import settings_premium as sp
import error
import http


class Premium:
    def __init__(self, access_token, websso_cookie):
        self.base_url = sp.base_url
        self.client_key = sp.client_key
        self.user_msisdn = sp.user_msisdn
        self.user_id = sp.user_id
        self.user_refresh_token = sp.user_refresh_token
        self.access_token = access_token
        self.websso_cookie = websso_cookie



    def get_available_msisdn_external(self):

        headers = {'x-token': self.client_key}

        response = requests.get(self.base_url + '/api/mhsrv/v1/external/subscriptions/available/' + self.user_msisdn, headers=headers, verify=False)
        status = response.status_code
        if (status != http.HTTPStatus.OK):
            return error.CustomError('server response ', status)

        try:
            result = response.json()
        except:
            return error.CustomError('error while json unserialization')

        return status, result

    def get_active_msisdn_external(self):

        headers = {'x-token': self.client_key}

        response = requests.get(self.base_url + '/api/mhsrv/v1/external/subscriptions/active/' + self.user_msisdn, headers=headers, verify=False)
        status = response.status_code
        if status != http.HTTPStatus.OK:
            return error.CustomError('server response ', status)

        try:
            result = response.json()
        except:
            return error.CustomError('c')

        return status, result

    def get_profiles_msisdn_external(self):

        headers = {'x-token': self.client_key}

        response = requests.get(self.base_url + '/api/user/v1/external/profile/' + self.user_msisdn, headers=headers, verify=False)
        status = response.status_code
        if (status != http.HTTPStatus.OK):
            return error.CustomError('server response ', status)

        try:
            result = response.json()
        except:
            return error.CustomError('error while json unserialization')

        return status, result

    def get_available_external(self):

        headers = {'x-token': self.client_key}
        params = {
            "userID": self.user_id
        }

        response = requests.get(self.base_url + '/api/mhsrv/v1/external/subscriptions/available/', params=params, headers=headers, verify=False)
        status = response.status_code
        if (status != http.HTTPStatus.OK):
            return error.CustomError('server response ', status)

        try:
            result = response.json()
        except:
            return error.CustomError('error while json unserialization')

        return status, result

    def get_active_external(self):

        headers = {'x-token': self.client_key}
        params = {
            "userID": self.user_id
        }

        response = requests.get(self.base_url + '/api/mhsrv/v1/external/subscriptions/active/', params=params, headers=headers, verify=False)
        status = response.status_code
        if (status != http.HTTPStatus.OK):
            return error.CustomError('server response ', status)

        try:
            result = response.json()
        except:
            return error.CustomError('error while json unserialization')

        return status, result

    def get_profiles_external(self):

        headers = {'x-token': self.client_key}

        response = requests.get(self.base_url + '/api/user/v1/external/profile/' + self.user_msisdn + '/status', headers=headers, verify=False)
        status = response.status_code
        if (status != http.HTTPStatus.OK):
            return error.CustomError('server response ', status)

        try:
            result = response.json()
        except:
            return error.CustomError('error while json unserialization')

        return status, result

    def profiles(self):
        headers = {'x-token': self.client_key}
        cookies = {'access_token': self.access_token, 'MTSWebSSO': self.websso_cookie}

        response = requests.get(self.base_url + '/api/user/v1/profile' , cookies=cookies, headers=headers, verify=False)

        status = response.status_code


        if (status != http.HTTPStatus.OK):
            return error.CustomError('server response ', status)

        try:
            result = response.json()
        except:
            return error.CustomError('error while json unserialization')

        return status, result

