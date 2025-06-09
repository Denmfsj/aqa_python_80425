class Course:

    def __init__(self, name: str, students: list = None, durations: int = 6):
        self.name = name
        self.students = students or []  # bool(students) - якщо це false, то []
        self.durations = durations

    def __str__(self):
        return f'instance of Course: {self.name} with {len(self.students)} for {self.durations} months'

    def __repr__(self):
        return f'Course(name="{self.name}", students={self.students}, durations={self.durations})'

    def __len__(self):
        return self.durations


math = Course('math', ['Viktor'])
print(len(math))  # math.__len__()


# logging.info(f"cur values = {str(math)}")  # print(str(math))
# str(math) # math.__str__()
# print(str(math))  # print(str(math))
# print(math.__str__())
#
# print(repr(math))  # math.__repr__()
#
# new_c = Course(name="math", students=['Viktor'], durations=6)