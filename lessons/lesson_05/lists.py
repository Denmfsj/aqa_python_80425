# списки
my_friends = ['Den']  #  словник з 1 елемента

my_list_of_items = ['Den', my_friends, 1, None, (1,2,3), False, 22.55, 1, 1]


# print(my_list_of_items[0])
# print(my_list_of_items[-1])
# print(my_list_of_items[2:8])
#
# print(my_list_of_items.index(1))
# print(my_list_of_items.count(1))
# print(id(my_list_of_items[:]))
# print(id(my_list_of_items))


# copy
# my_list_of_items_new = my_list_of_items[:]  # зробити поверхневу копію


# append, extend, insert

# my_list_of_items_new.append('new_value')
my_list_of_items.append('old_value')
# print(my_list_of_items)
# print(my_list_of_items_new)
new_list_whatever = [1,312]
my_list_of_items = ['Den', my_friends, 1, None, (1,2,3), False, 22.55, 1, 1]
# my_list_of_items.append(['Yuri', 'Mor'])
# print(my_list_of_items[-1])
# my_list_of_items.extend(['Yuri', 'Mor'])
# print(my_list_of_items)
# print(my_list_of_items[-1])
# my_list_of_items.extend(['Yuri', 'Mor'])

# new_var_as_a_res_of_append = new_list_whatever.append(123)  # new_var_as_a_res_of_append = None

# my_list_of_items.append(new_list_whatever.append(123))
# print(my_list_of_items)
# print(new_list_whatever)

# print(new_list_whatever)
# new_list_whatever.extend([1,2,3])  # new_list_whatever.append(1), new_list_whatever.append(2), new_list_whatever.append(3)
# print(new_list_whatever)
# new_list_whatever.extend('red')
# print(new_list_whatever)
#
# # for k in [1,2,3]:
# new_list_whatever.insert(-1 + 1, ['very_first_el', 'second'])
#
# print(new_list_whatever)


# видалення
my_list_of_items = ['Den', 1, None, (1,2,3), False, 22.55, 1, 1]


print(my_list_of_items)
# my_list_of_items.remove(22.55)
# print(my_list_of_items)

# pop
# my_list_of_items.pop(-3)  #  видалення по індексу 3 з кінця
# my_list_of_items.pop()  #  видалення останнього
# my_list_of_items.pop()  #  видалення останнього
# my_list_of_items.pop()  #  видалення останнього

last_value = my_list_of_items.pop(-4)
print(my_list_of_items)
print(last_value)

# my_list_of_items_new = my_list_of_items[:3] + my_list_of_items[6: ]
# print(my_list_of_items_new)

google_doc = ['id', '', 'name', '', '', '']

#
# while True:
#     if google_doc[-1] != '':
#         break
#     google_doc.pop()
#
# print(google_doc)


