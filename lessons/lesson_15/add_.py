import copy

class Course:

    def __init__(self, name: str, students: list):

        self.name = name
        self.students = students


    def __add__(self, other):

        if isinstance(other, Course):
            self.name = self.name + other.name #  .extend(other.students)  # [1,2].extend([3,4]) == [1,2,3,4]
        if isinstance(other, list):
            self.students.extend(other)
        if isinstance(other, int):
            self.len_of_course = other

        # new_list = copy.copy(self.students)
        # new_list.extend(other.students)
        # return Course('sum_of_2', new_list)




math = Course('math', ['Max', 'Yuri'])
lith = Course('lith', ['Den', 'Anna'])

# print(math.students)
# math + lith
# print(math.name)
# math + [1,2,3]
# print(math.students)
# math + 8
# print(math.len_of_course)

# print(math.students)
# math + lith  # math.__add__(lith)
# print(math.name)
# print(math.students)
# # print(new_c.name)
# print(new_c.students)
# print(math.students)