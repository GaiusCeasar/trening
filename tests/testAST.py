from astlab import ASTLab
from settingast import valid_login, valid_password
from pytest_html.extras import json

pf = ASTLab()


def test_get_api_key_valid_user(login=valid_login, password=valid_password):
    status, result = pf.get_token(login, password)
    assert status == 200
    assert 'token' in result
    print(result)


def test_get_all_applications():
    _, authorization = pf.get_token(valid_login, valid_password)
    status, result = pf.get_all_applications(authorization)
    assert status == 200
    assert len(result['data']) > 0
    print(json(result))


def test_get_applications_by_params(fio='Хлопов Антон Сергеевич'):
    _, authorization = pf.get_token(valid_login, valid_password)
    status, result = pf.get_application_by_params(authorization, fio)
    print(result)
    test_client = result['data'][0]['client']
    test_fio = test_client['lastName'] + ' ' + test_client['firstName'] + ' ' + test_client['middleName']
    assert status == 200
    assert len(result['data']) == 1
    assert fio == test_fio
    print(test_fio)


def test_add_new_applications(client_id='1', agency_id='1', bank_code="sber", user_id=1, gender="male",
                              first_name="Иван", middle_name="Иванович",
                              last_name="Иванов", birthday="2020-01-01", medical_check_chronical=True,
                              employment_type="employment", employment_is_office=True,
                              mortgage_amount=0, mortgage_remaining_debt=0, interest_rate=0, start_date="2021-12-22",
                              end_date="2021-12-22",
                              insurance_term="12",
                              products="[{\"life\": [\"renis\", \"absolute\", \"pari\"]}, {\"property\": [\"renis\", "
                                       "\"absolute\", \"pari\"]}, {\"title\": [\"renis\", \"absolute\", \"pari\"]}]",
                              property_build_year="2015"):
    _, authorization = pf.get_token(valid_login, valid_password)
    status, result = pf.add_new_application(authorization, client_id, agency_id, bank_code, user_id, gender, first_name,
                                            middle_name,
                                            last_name, birthday, medical_check_chronical, employment_type,
                                            employment_is_office,
                                            mortgage_amount, mortgage_remaining_debt, interest_rate, start_date,
                                            end_date,
                                            insurance_term, products, property_build_year)
    assert status == 200
    assert result['products'] == products
