from api_premium import Premium



pr = Premium()



'''Тест available'''
def test_available():
    status, result = pr.get_available()
    assert status == 200
    assert 'result' in result