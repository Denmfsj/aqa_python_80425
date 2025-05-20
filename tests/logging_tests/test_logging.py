from core.projects.user_ms_requests import get_user_info
from core.projects.wallets_ms_requests import get_wallet_info


def test_get_user_data():
    get_user_info()


def test_get_wallet_data():
    get_wallet_info()
