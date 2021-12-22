import json

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

    def add_new_application(self, authorization, client_id, agency_id, bank_code, user_id, gender, first_name, middle_name,
                                  last_name, birthday, medical_check_chronical: bool, employment_type, employment_is_office: bool,
                                  mortgage_amount, mortgage_remaining_debt, interest_rate, start_date, end_date,
                                  insurance_term, products, property_build_year):

        data = {
                "client_id": client_id,
                "agency_id": agency_id,
                "bank_code": bank_code,
                "user_id": user_id,
                "gender": gender,
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "birthday": birthday,
                "medical_check_chronical": medical_check_chronical,
                "employment_type": employment_type,
                "employment_is_office": employment_is_office,
                "mortgage_amount": mortgage_amount,
                "mortgage_remaining_debt": mortgage_remaining_debt,
                "interest_rate": interest_rate,
                "start_date": start_date,
                "end_date": end_date,
                "insurance_term": insurance_term,
                "products": products,
                "property_build_year": property_build_year

        }
        headers = {'Authorization': 'Bearer ' + authorization['token']}

        res = requests.put(self.base_url + 'applications', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result
