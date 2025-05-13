first_row = 'Hello how are you ololo bla-bla'

second_row = 'Hello how are you ololo bla-bla'

second_row = second_row + 'aaa'  # first_row не зміниться

print('they are ==', first_row == second_row)
print('they are is', first_row is second_row)
print(id(first_row), id(second_row))

first_list = [1,2,3]
second_list = [1,2,3]

print('they are ==', first_list == second_list)
print('they are is', first_list is second_list)
print(id(first_list), id(second_list))