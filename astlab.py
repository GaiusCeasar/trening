import requests


class ASTLab:
    def __init__(self):
        self.base_url = "http://ipbackend-master.test.fast-system.ru/api/"

    def get_token(self, login, password):

        body = {
            'login': login,
            'password': password,
        }
        res = requests.post(self.base_url + 'auth/login', data=body)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_all_applications(self, authorization):

        headers = {'Authorization': 'Bearer ' + authorization['token']}

        res = requests.get(self.base_url + 'applications', headers=headers)
        status = res.status_code
        result = ' '

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_application_by_params(self, authorization, fio):
        filters = {'fio': fio
                   }
        headers = {'Authorization': 'Bearer ' + authorization['token']}

        res = requests.get(self.base_url + 'applications', headers=headers, params=filters)
        status = res.status_code
        result = ' '
        print(res.url)

        try:
            result = res.json()
        except:
            result = res.text
        return status, result
