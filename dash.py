import requests
from http import cookiejar
from bs4 import BeautifulSoup
from .constants import DiscogsConstants

jar = cookiejar.CookieJar()


def login(username=None, password=None):
    username = username or DiscogsConstants.username
    password = password or DiscogsConstants.password

    res = requests.get(DiscogsConstants.login_url, cookies=jar)

    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')

    form = soup.find('form', {'id': 'login-form'})

    inputs = form.findAll('input')

    login_params = {field['name']: field.get('value') for field in inputs}

    login_params['username'] = DiscogsConstants.username
    login_params['password'] = DiscogsConstants.password

    return requests.post(DiscogsConstants.login_url, login_params, cookies=jar)



import ipdb; ipdb.set_trace()

# for i in range(100):
#     print(i if i % 2 == 0 else 'NAH KID!')
# #
# # l = [1,2,3,4,5,6,7]
# #
# # l_pp = [el+1 for el in l]
# #
# # print(l_pp)
