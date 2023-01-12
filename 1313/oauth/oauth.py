import requests
import http
import error


class Oauth:

    def __init__(self, client_id, client_secret, redirect_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url


    def get_auth_data(self, refresh):

        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_url,
        }

        token_url = 'https://login.mts.ru/amserver/oauth2/access_token'
        session = requests.Session()
        response = session.post(
            token_url, headers=headers, data=data, verify=False)

        status = response.status_code
        if (status != http.HTTPStatus.OK):
            return error.CustomError('server response ', status)

        try:
            result = response.json()
            access = result['access_token']
            print(access)
        except:
            return error.CustomError('error while json unserialization')

        url = 'https://login.mts.ru/amserver/oauth2/sso?at=' + access + \
              '&redirect_uri=https://dev-premium.mts.ru/api/user/v1/sso/login'
        response = session.get(url, verify=False)

        status = response.status_code
        if (status != http.HTTPStatus.OK):
            return error.CustomError('server response ', status)
            
        cookies = session.cookies.get_dict()
        premAccess, webSSO = cookies['access_token'], cookies['MTSWebSSO']
        if (premAccess == '' or webSSO == ''):
            return error.CustomError('premAccess or webSSO is an empty string')

        return premAccess, webSSO

