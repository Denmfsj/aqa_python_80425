
class Employee:

    def __init__(self):
        self.__current_personal = []
        self.__iter_current_element = 0

    def add_person(self, name):

        self.__current_personal.append(
            {
                'id': len(self.__current_personal) + 1,
                'name': name
            })

    def get_personal(self):
        return self.__current_personal


    def __iter__(self):
        return self

    def __next__(self):
        if self.__iter_current_element < len(self.__current_personal):
            person = self.__current_personal[self.__iter_current_element]
            self.__iter_current_element += 1
            return person
        raise StopIteration

    def __str__(self):
         return f'Інстанс з id {id(self)}'

empl = Employee()


for person in empl:
    print(person)

# empl.add_person('Den')
# empl.add_person('Ivan')
#
# empl_iterator = iter(empl)  # empl.__iter__() повинно повернути щось, у чого є __next__
#
# print(next(empl))  # empl.__next__()
# print(empl.__next__())

#
# for person in empl:
#     print(person)





#
# my_dct = {1:2, 3:4}
# for key in my_dct:
#     print(key)