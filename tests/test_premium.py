from api_premium import Premium
import json

pr = Premium()


'''Тест available{msisdn}'''
def test_available_msisdn():
    status, result = pr.get_available_msisdn()
    assert status == 200
    assert 'subscriptions' in result


'''Тест active_subscription{msisdn}'''
def test_active_subscription_msisdn():
    status, result = pr.get_active_msisdn()
    assert status == 200
    assert 'subscriptions' in result

'''Тест profiles{msisdn}'''
def test_profiles_msisdn():
    status, result = pr.get_profiles_msisdn()
    assert status == 200
    assert 'status' in result
    assert result['subscription'] == 'individual' or result['subscription'] == ''
    assert result['status'] == 1 or result['status'] == 0


'''Тест available_userID'''
def test_available():
    status, result = pr.get_available()
    assert status == 200
    assert 'subscriptions' in result


'''Тест active_subscription_userID'''
def test_active_subscription():
    status, result = pr.get_active()
    assert status == 200
    assert 'subscriptions' in result


'''Тест profiles_msisdn_status'''
def test_profiles():
    status, result = pr.get_profiles()
    assert status == 200
    assert 'status' in result
    assert result['status'] == 1 or result['status'] == 0
