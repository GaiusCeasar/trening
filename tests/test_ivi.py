from api2 import Ivi



pf = Ivi()

'''Тест авторизации'''
def test_get_basic_auth():
    status, result = pf.get_basic_auth()
    assert status == 200
    assert 'key' in result

'''Тест получения списка пользователей'''
def test_get_all_hero():
    status, result = pf.get_list_of_hero()
    assert status == 200
    assert 'result' in result

def test_get_all_pets_with_valid_key(name='Avalanche'):
    status, result = pf.get_list_hero_by_name(name)
    assert status == 200
    assert result ['Avalanche'] == name