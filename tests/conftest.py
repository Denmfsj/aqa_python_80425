import pytest


@pytest.fixture(autouse=True, scope='session')
def send_data_to_cloud():
    print('Clenup of some files')
    yield
    print('Sending data to cloud')


