import requests
from settings import auth
from requests_toolbelt.multipart.encoder import MultipartEncoder

class Ivi:
    def __init__(self):
        self.base_url = "http://rest.test.ivi.ru/v2/"

    def get_basic_auth(self):

        '''указываем параметры запроса'''
        res = requests.get(self.base_url, auth=auth)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_hero(self):

        res = requests.get(self.base_url + 'characters', auth=auth)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_hero_by_name(self, name):

        data = MultipartEncoder(
        fields=
        {'name': name})

        res = requests.get(self.base_url + 'characters', auth=auth, data=data)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result