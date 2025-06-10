# класс який вміє надсилат запити

class RequestHandler:


    def send_request(self, url, params, **kwargs):

        print(f'Sending requests to {url} with {params}...{kwargs}')


class UserEndpoints:

    def __init__(self, base_url):
        self.base_url = base_url

    USER_DETAILS  = '{base_url}/user/{user_id}'

    def get_url(self, url_str, **kwargs):
        return url_str.format(base_url=self.base_url, **kwargs)



class UserCtrlVersion2(RequestHandler):

    def __init__(self, base_url='127.0.0.1'):
        self.endpoints = UserEndpoints(base_url)  # bridge

    def get_user_details(self, user_id, full_details=False):
        url = self.endpoints.get_url(self.endpoints.USER_DETAILS, user_id=user_id)

        auth_header = ''

        return self.send_request(url=url,
                                 params={'full_details': full_details},
                                 auth_header=auth_header)




# class UserCtrlVersion1(RequestHandler, UserEndpoints):
#
#     def __init__(self, base_url='127.0.0.1'):
#         UserEndpoints.__init__(self, base_url)
#
#
#     def get_user_details(self, user_id, full_details=False):
#
#         url = self.get_url(self.USER_DETAILS, user_id=user_id)
#
#         auth_header = ''
#
#         return self.send_request(url=url, params={'full_details': full_details}, auth_header=auth_header)
#
#
#     def post_user_details(self, user_id, full_details=False):
#
#         url =f'127.0.0.1{self.get_url(self.USER_DETAILS, user_id=user_id)}'
#         return self.send_request(url=url, params={'full_details': full_details})
#
# usr_ctrl = UserCtrl()
# usr_ctrl.get_user_details(8)
#
#

# print(UserEndpoints.USER_DETAILS)
# url = '/user/{user_id}'
# url = url.format(user_id=8)
# print(url)
#
# UserEndpoints.get_url(UserEndpoints.USER_DETAILS, a=1, g=6, user_id=59)
#
# UserEndpoints.USER_DETAILS.format(a=1, g=6, user_id=59)
