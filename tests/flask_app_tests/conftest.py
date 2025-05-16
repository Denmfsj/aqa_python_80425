# import requests
# import pytest
#
# base_url = 'http://127.0.0.1:7070'
#
# all_content_url = f'{base_url}/content'
# content_by_id_url = all_content_url + '/{}' # http://127.0.0.1:7070/content/{}
# print(content_by_id_url)
#
#
# @pytest.fixture
# def add_specific_content():
#     specific_content = {'cars': ['Audi, VW', 'Toyota']}
#     requests.post(all_content_url, json=specific_content)