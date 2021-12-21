from astlab import ASTLab
from settingast import valid_login, valid_password

pf = ASTLab()


def test_get_api_key_valid_user(login=valid_login, password=valid_password):
    status, result = pf.get_token(login, password)
    assert status == 200
    assert 'token' in result
    print(result)
