
col = ['id', 1,2,3,4,5,6]

# name, *second_el, values = col  # id, [1,2,3,4,5], 6
# print(name)
# print(second_el)
# print(values)
#
# name, second_el, *values = col  # # id, 1 [2,3,4,5,6]
# print(name)
# print(second_el)
# print(values)
#
# *name, second_el, values = col  # [id, 1 2,3,4],5,6
# print(name)
# print(second_el)
# print(values)


# col = ['id', 1,2]
#
# name, first, second = col
#
# print(name)
# print(first)
# print(second)

# first = 1
# second = 2
#
# first, second = second, first  # зміна значень між змінними місцями
#
# print(second)
#
# col = ['id', 1,2,3,4,5,6]
# new_col = [col[2], col[3], col[0], col[-1]]
# print(new_col)