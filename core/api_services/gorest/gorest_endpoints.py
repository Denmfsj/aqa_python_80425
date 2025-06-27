import requests

class GorestEndpoint:

    base_url = 'https://gorest.co.in'
    public_part = f'{base_url}/public'
    version2 =  f'/v2'
    version1 =  f'/v1'


    def get_users(self, expected_status_code=200):
        response = requests.get(url=f'{self.get_path()}/users')

        # if response.status_code == 301:
        #     assert response.headers['redirect_url'].startswith('your_domain.com')
        #
        # assert response.url.startswith('your_domain.com')

        assert response.status_code == expected_status_code, \
            f'Status code is not 200, but {response.status_code}'
        return response


    def get_user(self, user_id, url_version=None, expected_status_code=200):

        url = f'{self.get_path(url_version)}/users'
        print(f'Sending request to {url}')

        response =  requests.get(url=f'{url}/users', params={'id': user_id})

        assert response.status_code == expected_status_code, \
            f'Status code is not 200, but {response.status_code}'
        return response

    def create_user(self, user_data, expected_status_code=201):
        response = requests.post(url=f'{self.get_path()}/users', json=user_data, headers={
            "Authorization": "Bearer ea1cf6a5c93238bfcd0c086b790f2353ff4418d899c26f8b9e8906a190c1111e"})

        assert response.status_code == expected_status_code, \
            f'Status code is not 201, but {response.status_code}'
        return response




    def get_path(self, version=None):
        if version is None:
            version = self.version2
        return f'{self.public_part}{version}'

