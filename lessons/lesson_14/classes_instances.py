class Phone:


    def __init__(self, number, operator, os_version='18.2'):  # метод конструктор
        self.my_number = number  # змінна/атрибут інстанса
        self.operator = operator
        self.some_f = None
        self.default_country = 'Ukraine'
        self.os_version = os_version


    def make_calls(self, number):  # метод інстанса класса
        print(f'Calling from {self.my_number} to {number}')

    def send_sms(self, number, text):
        print(f'Sending from {self.my_number} to {number}:\n{text}')

class IPhone(Phone):
    def __init__(self, number, operator):  # метод конструктор
        super().__init__(number=number, operator=operator, os_version=100)


    def make_calls(self, number):
        print('You are using Iphone')
        super().make_calls(number)

class Samsung(Phone):
    pass


i15 = IPhone('i15_number_123', 'life')
# i12 = IPhone('i12_number_456', 'kyivstar', os_version='16.5')

i15.make_calls(number=123)  # Phone.make_calls(self=i15, number=123)
print(i15.os_version)

# i12.make_calls(123)






# print(i15.os_version)
# print(i12.os_version)
# print(i15.my_number)
# print(i15.operator)
# print(i15.default_country)
# print(i15.os_version)
#
# print(i12.my_number)
# print(i12.operator)

#
# print(id(i15))
# print(id(i12))