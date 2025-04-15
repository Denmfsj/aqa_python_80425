# не мутабельні: int, str, tuple, bool, float
# мутабельні: list, dict, set

my_name = 'Denys'
your_name = my_name  # дивиться на місце в пам'яті де лежить my_name ЗАРАЗ

print('my_name', my_name, id(my_name))
print('your_name',your_name,  id(your_name))

my_name = my_name + 'a'

print('my_name', my_name, id(my_name))
print('your_name',your_name,  id(your_name))

my_list = [1,2,3]  #  список, list
print(my_list, id(my_list))
my_list.append(4)  # додати в список число 4

print(my_list, id(my_list))

