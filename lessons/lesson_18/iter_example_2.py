class Departments:

    def __init__(self, name):
        self.name = name


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


    def __next__(self):
        if self.__iter_current_element < len(self.__current_personal):
            person = self.__current_personal[self.__iter_current_element]
            self.__iter_current_element += 1
            return person
        raise StopIteration


class Office:

    def __init__(self):
        self.departments = []
        self.empls = Employee()


    def get_personal(self):
        return self.empls.get_personal()

    def add_person(self, name):

        self.empls.add_person(name)

    def __iter__(self):
        return self.empls



my_office = Office()

my_office.add_person('Den')
my_office.add_person('Ivan')

o_iter = iter(my_office) # my_office.__iter__()  => my_office.empls
next(o_iter)  # next(my_office.empls) => my_office.empls.__next__()

for person in my_office:
    print(person)





#
# my_dct = {1:2, 3:4}
# for key in my_dct:
#     print(key)