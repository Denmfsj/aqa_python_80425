import requests
from requests.auth import HTTPBasicAuth


resp = requests.post(url='http://127.0.0.1:8080/auth', auth=requests.auth.HTTPBasicAuth(username='test_user', password='test_pass')).json()
print(resp)

resp = requests.get(url='http://127.0.0.1:8080/cars?limit,sort_by', params={'limit': 10},
                     headers={'Authorization': f'Bearer {resp["access_token"]}'}).json()

print(resp)
