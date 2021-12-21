import requests


class ASTLab:
    def __init__(self):
        self.base_url = "http://ipbackend-master.test.fast-system.ru/"

    def get_token(self, login, password):

        body = {
           'login': login,
           'password': password,
          }
        res = requests.post(self.base_url + 'api/auth/login', data=body)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result