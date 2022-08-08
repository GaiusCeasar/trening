from api_premium import Premium



pr = Premium()



'''Тест available{msisdn}'''
def test_available():
    status, result = pr.get_available()
    assert status == 200
    assert 'subscriptions' in result
    print(result)