import requests


class StudentController:

    def __init__(self):

        self.base_url = 'http://127.0.0.1:8080/'
        self.token = None
        self.student_part = f'{self.base_url}students/'

        self._get_token_auth()


    def get_students(self, params=None):

        return requests.get(url=f'{self.student_part}', params=params)


    def get_student(self, student_id: int):
        return requests.get(url=f'{self.student_part}{student_id}')


    def create_student(self, student_data: dict):

        headers = {'token': self.token}

        return requests.post(url=f'{self.student_part}', data=student_data, headers=headers)


    def _get_token_auth(self):
        if self.token is None:
            self.token = requests.get(url=f'{self.base_url}auth/').text

