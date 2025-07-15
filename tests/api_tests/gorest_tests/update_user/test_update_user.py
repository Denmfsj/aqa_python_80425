import os

import pytest


@pytest.mark.usefixtures(f"get_user_on_{os.environ['current_env']}")
def test_update_user(session_user, get_user):

    ...


@pytest.fixture
def get_user():
    if os.environ['current_env'] == 'dev':
        return get_user_on_dev()

    if os.environ['current_env'] == 'stage':
        return get_user_on_stage()

def get_user_on_prod():
    pass

def get_user_on_stage():
    pass

def get_user_on_dev():
    pass