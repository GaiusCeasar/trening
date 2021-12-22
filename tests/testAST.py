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

