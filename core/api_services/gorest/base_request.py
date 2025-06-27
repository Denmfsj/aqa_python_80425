import requests

class BaseRequest:


    def send_request(self, method, url, exp_status_code, **kwargs):
        response = getattr(requests, method)(url=url, **kwargs)

        assert response.status_code == exp_status_code
        return response

#
# b_req = BaseRequest()
#
#
# url = 'https://gorest.co.in/public/v2/users'
# rs = b_req.send_request(url=url, method='delete', exp_status_code=405)
