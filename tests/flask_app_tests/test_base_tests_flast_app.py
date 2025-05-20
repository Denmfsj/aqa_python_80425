import requests
import pytest

base_url = 'http://127.0.0.1:7070'
content = {'cars': ['Audi, VW', 'Toyota']}

list_of_content = [
    {'cars': ['Audi']},
    {'cars': ['Audi, BMW']},
    {'cars': ['Audi', 'Toyota']},
    {'cars': ['Toyota']},
]

updated_content = {'bikes': ['Honda', 'Suzuki']}

all_content_url = f'{base_url}/content'
content_by_id_url = all_content_url + '/{}' # http://127.0.0.1:7070/content/{}


@pytest.mark.positive
class TestContent:

    test_1_result = None


    @pytest.fixture
    def add_specific_content(self):  # прекондішен для тестів в яких використовуеться ця функція
        specific_content = {'cars': ['Audi, VW', 'Toyota']}
        requests.post(all_content_url, json=specific_content)  # додавати на сервер specific_content



    # 1
    @pytest.mark.parametrize('j_content', list_of_content)
    def test_add_content(self, j_content):

        loggin.info(f'Sending request to {all_content_url}')
        response_data = requests.post(all_content_url, json=j_content)
        loggin.info(f'response has status code {response_data.status_code}')

        if response_data.status_code != 200:
            logging.error('status is not 200')
        assert response_data.json().get('message') == 'Content created successfully!'


        __class__.test_1_result = 'Alex'

    # 2
    @pytest.mark.depends(on=['test_add_content'])
    def test_get_content(self, add_specific_content):  # перед тестом буде виконана функція add_specific_content
        print('Getting content...')
        response_get = requests.get(all_content_url)
        assert response_get.status_code == 200, "Unable to get content"
        server_content = response_get.json().get('content')
        assert content in server_content

        assert __class__.test_1_result == 'Alex'

    # 4
    @pytest.mark.depends(on=['test_deleting_content'])
    def test_modify_content(self, add_specific_content):
        print('Modifying content...')
        response = requests.put(content_by_id_url.format('0'), json=updated_content)
        assert response.status_code == 200, "Unable modify content"
        assert response.json().get('message') == 'Content updated successfully!'

    # 3
    @pytest.mark.depends(on=['test_get_content'])
    @pytest.mark.smoke
    def test_deleting_content(self, add_specific_content):
        print('Deleting content...')
        response = requests.delete(f'{base_url}/content/0')
        assert response.status_code == 200, "Unable delete content"
        assert response.json().get('message') == 'Content deleted successfully!'
