# https://swapi.info/api/films/
# https://gorest.co.in/public/v2/users?id=7966026  Jagadish

import requests

#
# response_123 = requests.get(url='https://swapi.info/api/films/')
#
# # response = requests.get(url='https://gorest.co.in/public/v2/users?name=Jagadish')
# response = requests.get(url='https://gorest.co.in/public/v2/users',
#                         params={'name': 'Jagadish'})


# "Authorization": "Bearer ea1cf6a5c93238bfcd0c086b790f2353ff4418d899c26f8b9e8906a190c1111e"

#

#
# response = requests.post(url='https://gorest.co.in/public/v2/users',
#                          json={"name":"Tenali Ramakrishna", "gender":"male",
#                                "email":"tenali.ramakrishna@15123123123ce.com", "status":"active"},
#                          headers={"Authorization": "Bearer ea1cf6a5c93238bfcd0c086b790f2353ff4418d899c26f8b9e8906a190c1111e"})
#
# print(response.status_code)
# print(response.json())


# print('status_code', response_123.status_code)
# print('url', response_123.url)
# print('headers', dict(response_123.headers))
# # print('text', response_123.text)
# print('json', response_123.json())  # json.loads(response_123.text)
#
# print(response_123)