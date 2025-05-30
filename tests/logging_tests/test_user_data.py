from constants import USER_DATA_PROD

def check_user_data():

    with open(USER_DATA_PROD) as f:
        user_data = f.read()