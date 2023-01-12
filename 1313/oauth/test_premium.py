from api_premium import Premium
import urllib3
import oauth
import settings_premium as sp
import error
import http

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth = oauth.Oauth(sp.auth_client_id, sp.auth_client_secret, sp.redirect_uri)

try:
    access, websso_cookie = auth.get_auth_data(sp.user_refresh_token)
except error.CustomError as e:
    raise print('get_auth_data err ' + e)


pr = Premium(access, websso_cookie)
try:
    status, result = pr.profiles()
except error.CustomError as e:
    raise print('get_auth_data err ' + e)


'''Тест available{msisdn}'''


def test_available_msisdn_external():
    status, result = pr.get_available_msisdn_external()
    assert status == http.HTTPStatus.OK
    assert 'subscriptions' in result


'''Тест active_subscription{msisdn}'''


def test_active_subscription_msisdn_external():
    status, result = pr.get_active_msisdn_external()
    assert status == http.HTTPStatus.OK
    assert 'subscriptions' in result


'''Тест profiles{msisdn}'''


def test_profiles_msisdn_external():
    status, result = pr.get_profiles_msisdn_external()

    assert status == http.HTTPStatus.OK
    assert 'status' in result

    sub = result['subscription']
    status = result['status']

    assert result['subscription'] == 'individual' \
           or result['subscription'] == '' \
           or result['subscription'] == 'family_member' \
           or result['subscription'] == 'family_sponsor' and result['family'] == {'isSponsor': True}
    assert status == 1 or status == 0


'''Тест available_userID'''


def test_available_external():
    status, result = pr.get_available_external()
    assert status == http.HTTPStatus.OK
    assert 'subscriptions' in result


'''Тест active_subscription_userID'''


def test_active_subscription_external():
    status, result = pr.get_active_external()
    assert status == http.HTTPStatus.OK
    assert 'subscriptions' in result


'''Тест profiles_msisdn_status'''


def test_profiles_external():
    status, result = pr.get_profiles_external()
    assert status == http.HTTPStatus.OK
    assert 'status' in result

    status = result['status']
    assert status == 1 or status == 0

'''внутренний профайл'''
def test_profiles():
    status, result = pr.profiles()
    assert status == http.HTTPStatus.OK
    assert 'status' in result


# test_available_msisdn()
# test_active_subscription_msisdn()
# test_profiles_msisdn()
# test_available()
# test_active_subscription()
# test_profiles()
# test_profile()
