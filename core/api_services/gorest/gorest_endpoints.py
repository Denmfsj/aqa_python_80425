import requests

from curlify import to_curl

from core.api_services.gorest.schemas.user_schema import UserSchema


class GorestEndpoint:

    base_url = 'https://gorest.co.in'
    public_part = f'{base_url}/public'
    version2 =  f'/v2'
    version1 =  f'/v1'


    def get_users(self, params=None, expected_status_code=200, validate_schema=True):

        response = requests.get(url=f'{self.get_path()}/users', params=params)

        print(to_curl(response.request))
        print(f'Status code is {response.status_code}')


        assert response.status_code == expected_status_code, \
            f'Status code is not 200, but {response.status_code}'

        if validate_schema:
            print('Validating schema')
            UserSchema(many=True).load(response.json())
        return response


    def get_user(self, user_id, url_version=None, expected_status_code=200, validate_schema=True):

        url = f'{self.get_path(url_version)}/users/{user_id}'
        print(f'Sending request to {url}')

        response =  requests.get(url=url)
        print(to_curl(response.request))
        print(f'Status code is {response.status_code}')

        assert response.status_code == expected_status_code, \
            f'Status code is not 200, but {response.status_code}'
        if validate_schema:
            print('Validating schema')
            UserSchema(many=True).load(response.json())
        return response

    def create_user(self, user_data, header=None, expected_status_code=201):

        if header is None:
            header={
                "Authorization": "Bearer ea1cf6a5c93238bfcd0c086b790f2353ff4418d899c26f8b9e8906a190c1111e"
            }

        response = requests.post(url=f'{self.get_path()}/users', json=user_data, headers=header)
        print(to_curl(response.request))
        print(f'Status code is {response.status_code}')

        assert response.status_code == expected_status_code, \
            f'Status code is not {expected_status_code}, but {response.status_code}'
        return response


    def delete_user(self, user_id, header=None, expected_status_code=204):

        if header is None:
            header={
                "Authorization": "Bearer ea1cf6a5c93238bfcd0c086b790f2353ff4418d899c26f8b9e8906a190c1111e"
            }

        response = requests.delete(url=f'{self.get_path()}/users/{user_id}', headers=header)
        print(to_curl(response.request))
        print(f'Status code is {response.status_code}')

        assert response.status_code == expected_status_code, \
            f'Status code is not {expected_status_code}, but {response.status_code}'
        return response



    def get_path(self, version=None):
        if version is None:
            version = self.version2
        return f'{self.public_part}{version}'

