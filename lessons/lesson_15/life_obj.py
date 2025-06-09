class User:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'User {self.name} was deleted')


# ivan = User('ivan')
#
# # del ivan
# print('done')

