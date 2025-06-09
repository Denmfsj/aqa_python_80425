api_resp = {
    'data': [
        {'id': 5, 'name': 'ivan'},
        {'id': 6, 'name': 'Alex'},
        {'id': 7, 'name': 'Mor'},
    ],
    'valid_users': 8
}

class Users:

    def __init__(self, data, valid_users):
        self.user_details = data
        self.valid_users = valid_users

    def __len__(self):
        return len(self.user_details)

api_obj_resp = Users(**api_resp)  # Users(data = api_resp['data'], valid_users=api_resp['valid_users'])

assert len(api_obj_resp) > 0  # len(api_obj_resp) => api_obj_resp.__len__() => len(api_obj_resp.user_details)
