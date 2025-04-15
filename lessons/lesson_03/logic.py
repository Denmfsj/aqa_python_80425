# None, False, True, if, for

# false = False
#
# Or = 123


my_age = 20

my_father_age = 40

# result =  my_age > my_father_age  # result = False
# print('my_age > my_father_age', my_age > my_father_age)  # False
# print('my_age < my_father_age', my_age < my_father_age)  #  True
# print('20 <= 20', 20 <= 20)  #  True
# print('20 >= 20', 20 >= 20)  #  True
# print('19 >= 20', 19 >= 20)  #  True
#
# print('20 == 20', my_age == my_age)  #  True
# print('19 != 20', 19 != 20)  #  True не дорівнює
#
# db_data = [{'id': 20, 'name': 'Alex'}]
#
# # len(db_data) - довжина, кількість елементів в списку
#
# print('users in db more than 0', len(db_data) > 0)
# print('users in db more than 0', len(db_data) != 0)
#
# print('User with id=20 in db is 1 ', len(db_data) == 1)
# ------------------------

# print(22/2) # 11.0, повертає float
# print(21/2) # 10.5, повертає float
# print(20//3) # 6, повертає int(цілочисленне значення), просто відкидує число після коми
#
# print(20%3) # 20 / 3 = 16 + 2/3,  2, повертає int(цілочисленне значення), залишок від ділення
#
# # -------------------
#
# print(2**2)  # 4
# print(-5**2)  # -25
# print((-5)**2)  # 25
# print(-5**3)  # -125

# -----------------------------------
# and, or, not
# print(True and True)  # True
# print(True or True)  # True

# print(True and False)  # False
# print(True or False)  # True

# print(not True)  # False
# print(not False)  # True

my_age = 33
my_father_age = 70
my_son_age = 6

discount_min_age = 18
discount_max_age = 65

# discount if discount_min_age <= age <= discount_max_age

#
# print('I has discount:', (my_age >= discount_min_age) and (my_age <= discount_max_age))
# print('my_son_age has discount wrong calculation:',
#       (my_son_age >= discount_min_age) or (my_son_age <= discount_max_age))
#
# # (True or True) and (False or False) => True and False
# print((True or True) and (False or False))
# print(True or True and False or False)


# db_data = None
#
# if db_data is not None and db_data > 5:
# # if db_data > 5:
#     print('asd')

#
# if (my_age > discount_min_age) and (my_age < discount_max_age):
#     print('2 have discount ')

# (       )
# print(1, 2, 3)  # функція
# print(len('asd'))
#
# my_tuple = (1, 2, 3, 4, 'asd')  # tuple

# []

my_list = [1,2,3,4,5, 'asd']  # list
my_dict = {'id': 20, 'name': 'Ivan'}  # dict

print(my_list[-1])  # 'asd'
print(my_dict['name'])  # 'Ivan'

# {}
my_dict = {'id': 20, 'name': 'Ivan'}  # dict
#  в f-стоках
my_set = {20, 40, 50, 50, 20}  # set

print(my_set)


# :

if 20 > 40:
    print('20 > 40')

for char in 'asd':
    print('char')

def greetings():
    print('Hello')

# .
llt = [1,3,2]
llt.sort()
print(llt)
print(my_dict.get('name'))

# ;
llt = [1,3,2];

my_age, your_age = 20,  22
my_age = 20; your_age =  22

print(my_age)
print(your_age)


print(min('1', '2', '3', '56'))
print(max(1, 2, 3.0, len('asdasd'))) # len('asdasd') поверне int 6

print(len(str(21/2)))  # len(str(10.5))